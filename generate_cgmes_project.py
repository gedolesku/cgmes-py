#!/usr/bin/env python3
"""generate_dataclasses.py  –  CGMES 2.4 UML‑XMI → dataclasses
================================================================

‼️ Verzija 2025‑06‑04b – ispravka XPath‑a za **EA XMI export** bez prefiksa.

* `walk()` sada počinje od `<uml:Model>` čvora (ne od korena `<xmi:XMI>`).
* Svi XPath izrazi (`packagedElement`, `ownedAttribute`, `generalization`,
  `ownedEnd`) više **ne koriste prefiks** jer EA export ima elemente bez
  `uml:` prefiksa.
* Multipliciteti se čitaju iz atributa `<lowerValue>` / `<upperValue>` bez
  prefiksa.
* Dodati debug print‑ovi koje možeš isključiti `DEBUG = False`.

UML klase se često pojavljuju u više paketa.  Najpre se objedine sve
definicije sa istim XMI identifikatorom.  Zatim se dodatno spajaju
definicije koje imaju istu putanju paketa (npr. `Core::Topology`) i
isto ime klase.  Atributi i baze svih kopija se objedine, pa rezultujuća
dataclasses imaju veze iz svake pojavne lokacije.  Zbog toga npr.
`TopologicalNode` može sadržati asocijacije iz više paketa, čak i ako su
u Enterprise Architect modelu prikazane samo u jednom profilu.

Ako postoji UML `Dependency` link između dve klase, klasa na početku veze
dobija dodatnog roditelja.  Ako ciljna klasa ne postoji u XMI‑ju, pokušava
se pronalaženje druge klase sa istim `GUIDBasedOn` identifikatorom i ona se
koristi kao roditelj.  Tako `TopologyProfile.TopologicalNode` nasleđuje
`StateVariablesProfile.TopologicalNode` jer dele zajednički `GUIDBasedOn`.
Klase označene `isAbstract="true"` nasleđuju i `ABC` kako bi bile apstraktne
u generisanom Python kodu.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import keyword

from lxml import etree
from rdflib import Graph, Literal, Namespace, RDF, URIRef

DEBUG = False  # postavi True za obilne poruke

# ────────────────────────────────────────────────────────────────
#  Namespaces iz EA XMI
# ────────────────────────────────────────────────────────────────

UML_NS = "http://www.omg.org/spec/UML/20090901"
XMI_NS = "http://schema.omg.org/spec/XMI/2.1"
NSMAP = {"uml": UML_NS, "xmi": XMI_NS}

PRIMITIVE_MAP = {
    "Boolean": "bool",
    "Float": "float",
    "Integer": "int",
    "String": "str",
    "UnlimitedNatural": "int",
    "Decimal": "float",
    "DateTime": "str",
}

CIM = Namespace("http://iec.ch/TC57/2013/CIM-schema-cim#")

# ────────────────────────────────────────────────────────────────
#  Metapodaci
# ────────────────────────────────────────────────────────────────

@dataclass
class Attribute:
    name: str
    cim_path: str
    type_: str
    multiplicity: str
    is_ref: bool = False
    ref_pkg: Optional[Tuple[str, ...]] = None
    uml_id: Optional[str] = None  # XMI id, for tracking links
    target_id: Optional[str] = None  # referenced class XMI id


@dataclass
class ClassMeta:
    name: str
    attrs: Dict[str, Attribute]
    bases: List[str]
    pkg_parts: Tuple[str, ...]
    doc: Optional[str] = None
    base_pkgs: List[Tuple[str, ...]] = field(default_factory=list)
    uml_id: Optional[str] = None
    links: List["LinkData"] = field(default_factory=list)
    is_abstract: bool = False
    guid: Optional[str] = None


@dataclass
class EnumMeta:
    """Metadata for UML enumerations."""

    name: str
    literals: List[str]
    pkg_parts: Tuple[str, ...]
    doc: Optional[str] = None


@dataclass
class LinkData:
    """Minimal info about XMI links for later tooling."""

    uml_id: str
    kind: str
    start: str
    end: str

# ────────────────────────────────────────────────────────────────
#  Učitavanje XMI
# ────────────────────────────────────────────────────────────────

def _load_xmi(src: Path) -> etree._ElementTree:
    if not src.exists():
        raise FileNotFoundError(src)
    if src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src) as zf:
            name = next((n for n in zf.namelist() if n.lower().endswith((".xmi", ".xml"))), None)
            if not name:
                raise RuntimeError("ZIP ne sadrži .xmi/.xml")
            return etree.ElementTree(etree.fromstring(zf.read(name)))
    return etree.parse(str(src))

# ────────────────────────────────────────────────────────────────
#  Pomoćne
# ────────────────────────────────────────────────────────────────

def _mult_from_elem(elem: etree._Element) -> Tuple[str, str]:
    lower = elem.get("lower") or elem.get("lowerValue") or "1"
    upper = elem.get("upper") or elem.get("upperValue") or "1"
    if lower == "":
        lower = "1"
    if upper == "":
        upper = "1"
    if (lv := elem.find("lowerValue")) is not None:
        lower = lv.get("value") or lower
    if (uv := elem.find("upperValue")) is not None:
        upper = uv.get("value") or upper
    return lower, upper


def _sanitize(name: str) -> str:
    """Return *name* converted to a valid Python identifier."""
    if not name:
        name = "_"
    name = re.sub(r"\W", "_", name.strip())
    if not name or name[0].isdigit():
        name = f"_{name}"
    if keyword.iskeyword(name) or name in {"None", "True", "False"}:
        name = f"_{name}"
    return name


def _ptype(base: str, lower: str, upper: str) -> str:
    if upper == "*" or (upper.isdigit() and int(upper) > 1):
        return f"list[{base}]"
    if lower == "0":
        return f"Optional[{base}]"
    return base

# ────────────────────────────────────────────────────────────────
#  Parsiranje
# ────────────────────────────────────────────────────────────────

def _parse_xmi(tree: etree._ElementTree) -> Tuple[
    Dict[Tuple[str, ...], ClassMeta],
    Dict[Tuple[str, ...], EnumMeta],
    List[LinkData],
]:
    """Return class/enumeration metadata and parsed link info."""
    root = tree.getroot()
    by_id = {e.get(f"{{{XMI_NS}}}id"): e for e in root.iter() if e.get(f"{{{XMI_NS}}}id")}

    prim_elems = root.xpath(".//packagedElement[@xmi:type='uml:PrimitiveType']", namespaces=NSMAP)
    primitive_ids = {e.get(f"{{{XMI_NS}}}id"): PRIMITIVE_MAP.get(e.get("name")) for e in prim_elems}

    # pre-pass to determine package path for all elements
    def collect_pkgs(elem, pkg_path, out):
        for child in elem.xpath("./packagedElement"):
            kind = child.get(f"{{{XMI_NS}}}type")
            if kind == "uml:Package":
                collect_pkgs(child, pkg_path + [child.get("name")], out)
            else:
                out[child.get(f"{{{XMI_NS}}}id")] = tuple(pkg_path)

    id_to_pkg: Dict[str, Tuple[str, ...]] = {}
    for model in root.xpath(".//uml:Model", namespaces=NSMAP):
        collect_pkgs(model, [], id_to_pkg)

    classes: Dict[Tuple[str, ...], ClassMeta] = {}
    enums: Dict[Tuple[str, ...], EnumMeta] = {}
    class_by_id: Dict[str, List[ClassMeta]] = {}
    enum_by_id: Dict[str, EnumMeta] = {}
    attr_by_id: Dict[str, Tuple[ClassMeta, Attribute]] = {}
    links: List[LinkData] = []

    def walk(elem, pkg_path: List[str]):
        for child in elem.xpath("./packagedElement"):
            kind = child.get(f"{{{XMI_NS}}}type")
            if kind == "uml:Package":
                walk(child, pkg_path + [_sanitize(child.get("name"))])
                continue
            if kind == "uml:Enumeration":
                ename = _sanitize(child.get("name"))
                if DEBUG:
                    print("🔍 Enum", ename)
                e_doc = child.find("ownedComment/Body")
                key = tuple(pkg_path + [ename])
                literals = [_sanitize(l.get("name")) for l in child.xpath("./ownedLiteral")]
                meta = EnumMeta(
                    ename,
                    literals,
                    tuple(pkg_path),
                    e_doc.text if e_doc is not None else None,
                )
                enums[key] = meta
                enum_by_id[child.get(f"{{{XMI_NS}}}id")] = meta
                id_to_pkg[child.get(f"{{{XMI_NS}}}id")] = tuple(pkg_path)
                continue
            if kind != "uml:Class":
                continue
            cname = _sanitize(child.get("name"))
            if DEBUG:
                print("🔍 Klasa", cname)
                        # pokušaj docstringa
            c_doc = child.find("ownedComment/Body")
            guid = None
            tag = child.find("tags/tag[@name='GUIDBasedOn']")
            if tag is None:
                ref_elem = root.find(f".//element[@xmi:idref='{child.get(f'{{{XMI_NS}}}id')}']", namespaces=NSMAP)
                if ref_elem is not None:
                    tag = ref_elem.find("tags/tag[@name='GUIDBasedOn']")
            if tag is not None:
                val = tag.get("value", "").strip("{}")
                if val:
                    guid = val.replace('_', '-')
            meta = ClassMeta(
                cname,
                {},
                [],
                tuple(pkg_path),
                c_doc.text if c_doc is not None else None,
                [],
                child.get(f"{{{XMI_NS}}}id"),
                [],
                child.get("isAbstract") == "true",
                guid,
            )
            key = tuple(pkg_path + [cname])
            target = classes.get(key)
            if target is None:
                target = meta
                classes[key] = target
                class_by_id.setdefault(child.get(f"{{{XMI_NS}}}id"), []).append(target)
                id_to_pkg[child.get(f"{{{XMI_NS}}}id")] = tuple(pkg_path)
            else:
                if not target.doc and meta.doc:
                    target.doc = meta.doc

            # ownedAttribute
            for prop in child.xpath("./ownedAttribute"):
                a_name = _sanitize(prop.get("name"))
                type_ref = prop.get("type")
                if type_ref is None:
                    t_elem = prop.find("type")
                    if t_elem is not None:
                        type_ref = t_elem.get(f"{{{XMI_NS}}}idref")
                lower, upper = _mult_from_elem(prop)
                if type_ref in primitive_ids:
                    base_type = primitive_ids[type_ref]
                    ref_pkg = None
                elif type_ref in class_by_id:
                    base_type = class_by_id[type_ref][0].name
                    ref_pkg = class_by_id[type_ref][0].pkg_parts
                elif type_ref in enum_by_id:
                    base_type = enum_by_id[type_ref].name
                    ref_pkg = enum_by_id[type_ref].pkg_parts
                else:
                    base_type = by_id.get(type_ref).get("name") if type_ref in by_id else "str"
                    ref_pkg = id_to_pkg.get(type_ref)
                is_ref = bool(prop.get("association"))
                attr = Attribute(
                    a_name,
                    f"cim:{cname}.{a_name}",
                    _ptype(base_type, lower, upper),
                    f"{lower}..{upper}" if lower != upper else lower,
                    is_ref,
                    ref_pkg,
                    prop.get(f"{{{XMI_NS}}}id"),
                    type_ref,
                )
                target.attrs[a_name] = attr
                if attr.uml_id:
                    attr_by_id[attr.uml_id] = (target, attr)

            # generalization
            gen = child.find("generalization")
            if gen is not None and (gid := gen.get("general")):
                if gid in class_by_id:
                    pname = class_by_id[gid][0].name
                    ppkg = class_by_id[gid][0].pkg_parts
                else:
                    pname = by_id.get(gid).get("name") if gid in by_id else None
                    ppkg = id_to_pkg.get(gid)
                if pname:
                    if pname not in target.bases:
                        target.bases.append(pname)
                        target.base_pkgs.append(ppkg)

    # start from each uml:Model
    for model in root.xpath(".//uml:Model", namespaces=NSMAP):
        walk(model, [])

    # parse link information (Generalization, Association, ...)
    for link in root.xpath('.//element/links/*'):
        lid = link.get(f'{{{XMI_NS}}}id')
        start = link.get('start')
        end = link.get('end')
        kind = etree.QName(link).localname
        if lid and start and end:
            ldata = LinkData(lid, kind, start, end)
            links.append(ldata)
            if start in class_by_id:
                for meta in class_by_id[start]:
                    meta.links.append(ldata)
            if end in class_by_id:
                for meta in class_by_id[end]:
                    meta.links.append(ldata)

    # apply generalization and dependency links
    for lnk in links:
        if lnk.kind not in {'Generalization', 'Dependency'}:
            continue
        if lnk.start not in class_by_id:
            continue
        if lnk.end in class_by_id:
            candidates = class_by_id[lnk.end]
        else:
            guid = lnk.end.removeprefix('EAID_').replace('_', '-')
            candidates = [m for m in classes.values() if m.guid == guid]
        if not candidates:
            continue
        for child in class_by_id[lnk.start]:
            parent = next((c for c in candidates if c.pkg_parts != child.pkg_parts or c.name != child.name), None)
            if parent is None:
                continue
            if (
                lnk.kind == 'Dependency'
                and child.guid
                and parent.guid
                and child.guid == parent.guid
                and parent.name in child.bases
            ):
                # skip reverse inheritance when two classes share the same GUID
                continue
            if parent.name not in child.bases:
                child.bases.append(parent.name)
                child.base_pkgs.append(parent.pkg_parts)

    # associations
    for assoc in root.xpath(".//packagedElement[@xmi:type='uml:Association']", namespaces=NSMAP):
        member_ids = [m.get(f"{{{XMI_NS}}}idref") for m in assoc.xpath("./memberEnd")]
        owned_map = {e.get(f"{{{XMI_NS}}}id"): e for e in assoc.xpath("./ownedEnd")}
        if len(member_ids) != 2:
            continue
        for idx, end_id in enumerate(member_ids):
            other_id = member_ids[1 - idx]
            if end_id in attr_by_id:
                # attribute already created when walking class
                continue
            if end_id not in owned_map:
                continue
            end = owned_map[end_id]
            target_id = end.get("type")
            if target_id is None:
                t_elem = end.find("type")
                if t_elem is not None:
                    target_id = t_elem.get(f"{{{XMI_NS}}}idref")
            if other_id in attr_by_id:
                owner_class_id = attr_by_id[other_id][1].target_id
            elif other_id in owned_map:
                owner_class_id = owned_map[other_id].get("type")
                if owner_class_id is None:
                    t_elem = owned_map[other_id].find("type")
                    if t_elem is not None:
                        owner_class_id = t_elem.get(f"{{{XMI_NS}}}idref")
            else:
                owner_class_id = None
            if owner_class_id in class_by_id and target_id in class_by_id:
                target_meta = class_by_id[target_id][0]
                lower, upper = _mult_from_elem(end)
                for owner_meta in class_by_id[owner_class_id]:
                    aname = _sanitize(end.get("name") or target_meta.name)
                    owner_meta.attrs.setdefault(
                        aname,
                        Attribute(
                            aname,
                            f"cim:{owner_meta.name}.{aname}",
                            _ptype(target_meta.name, lower, upper),
                            f"{lower}..{upper}" if lower != upper else lower,
                            True,
                            target_meta.pkg_parts,
                            end.get(f"{{{XMI_NS}}}id"),
                            target_id,
                        ),
                    )

    # merge attributes and bases across duplicate class definitions by XMI id
    for metas in class_by_id.values():
        if len(metas) < 2:
            continue
        combined_attrs: Dict[str, Attribute] = {}
        bases: List[str] = []
        base_pkgs: List[Tuple[str, ...]] = []
        doc = None
        guid = None
        for m in metas:
            combined_attrs.update(m.attrs)
            for b, p in zip(m.bases, m.base_pkgs):
                if b not in bases:
                    bases.append(b)
                    base_pkgs.append(p)
            if m.doc and not doc:
                doc = m.doc
            if not guid and m.guid:
                guid = m.guid
        for m in metas:
            for a_name, attr in combined_attrs.items():
                m.attrs.setdefault(a_name, attr)
            for b, p in zip(bases, base_pkgs):
                if b not in m.bases:
                    m.bases.append(b)
                    m.base_pkgs.append(p)
            if doc and not m.doc:
                m.doc = doc
            if guid and not m.guid:
                m.guid = guid

    # merge classes that share the same package path and name
    path_groups: Dict[Tuple[str, ...], List[ClassMeta]] = {}
    for meta in classes.values():
        key = meta.pkg_parts + (meta.name,)
        path_groups.setdefault(key, []).append(meta)
    for metas in path_groups.values():
        if len(metas) < 2:
            continue
        combined_attrs: Dict[str, Attribute] = {}
        bases: List[str] = []
        base_pkgs: List[Tuple[str, ...]] = []
        doc = None
        guid = None
        for m in metas:
            combined_attrs.update(m.attrs)
            for b, p in zip(m.bases, m.base_pkgs):
                if b not in bases:
                    bases.append(b)
                    base_pkgs.append(p)
            if m.doc and not doc:
                doc = m.doc
            if not guid and m.guid:
                guid = m.guid
        for m in metas:
            for a_name, attr in combined_attrs.items():
                m.attrs.setdefault(a_name, attr)
            for b, p in zip(bases, base_pkgs):
                if b not in m.bases:
                    m.bases.append(b)
                    m.base_pkgs.append(p)
            if doc and not m.doc:
                m.doc = doc
            if guid and not m.guid:
                m.guid = guid

    print(
        "✅ klase:", len(classes), "– prim:", len(primitive_ids), "– enum:", len(enums)
    )
    return classes, enums, links
# ────────────────────────────────────────────────────────────────
#  Code writer
# ────────────────────────────────────────────────────────────────

def _rel_mod(src: Tuple[str, ...], dst: Tuple[str, ...], name: str) -> str:
    """Return relative module path for importing *name* located in *dst* when inside *src*."""
    common = 0
    for a, b in zip(src, dst):
        if a != b:
            break
        common += 1
    dots = '.' * (len(src) - common + 1)
    rest = '.'.join(dst[common:] + (name,))
    return f"{dots}{rest}"


def _py_imports(meta: ClassMeta, classes: Dict[Tuple[str, ...], ClassMeta], enums: Dict[Tuple[str, ...], EnumMeta]) -> Tuple[List[str], Dict[str, str]]:
    imps = {
        "from __future__ import annotations",
        "from dataclasses import dataclass, field",
        "from typing import Optional, List",
        f"from {'.' * (len(meta.pkg_parts) + 1)}base import CIMObject",
    }
    if meta.is_abstract:
        imps.add("from abc import ABC")
    alias_map: Dict[str, str] = {}
    for base, pkg in zip(meta.bases, meta.base_pkgs):
        if base == "CIMObject":
            continue
        if pkg == meta.pkg_parts and base == meta.name:
            # avoid self-import when dependency points to same class
            continue
        alias = base
        if base == meta.name and pkg != meta.pkg_parts:
            alias = f"{base}_base"
        if pkg and pkg != meta.pkg_parts:
            path = _rel_mod(meta.pkg_parts, pkg, base)
            if alias != base:
                imps.add(f"from {path} import {base} as {alias}")
            else:
                imps.add(f"from {path} import {base}")
        alias_map[base] = alias
    for a in meta.attrs.values():
        base = a.type_
        if base.startswith("Optional[") and base.endswith("]"):
            base = base[len("Optional["):-1]
        if base.startswith("list[") and base.endswith("]"):
            base = base[len("list["):-1]
        if base not in {"str", "int", "float", "bool"}:
            pkg = a.ref_pkg or meta.pkg_parts
            if base != meta.name or pkg != meta.pkg_parts:
                path = _rel_mod(meta.pkg_parts, pkg, base)
                imps.add(f"from {path} import {base}")

    return sorted(imps), alias_map

def _write_enums(enums: Dict[Tuple[str, ...], EnumMeta], out_dir: Path) -> int:
    """Write Enum classes for all UML enumerations."""
    cnt = 0
    for meta in enums.values():
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)
        partial = out_dir
        for part in meta.pkg_parts:
            partial /= part
            (partial / "__init__.py").touch(exist_ok=True)

        lines = ["from enum import Enum", "", f"class {meta.name}(Enum):"]
        for lit in meta.literals:
            lines.append(f"    {lit} = '{lit}'")
        if not meta.literals:
            lines.append("    pass")
        (pkg_dir / f"{meta.name}.py").write_text("\n".join(lines) + "\n", encoding="utf-8")
        cnt += 1
    return cnt


def _write_classes(classes: Dict[Tuple[str, ...], ClassMeta], enums: Dict[Tuple[str, ...], EnumMeta], out_dir: Path) -> int:
    """Write dataclass modules for all CGMES classes into *out_dir*.

    Returns the number of files written.
    """
    cnt = 0
    for meta in classes.values():
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)
        # ensure __init__.py
        partial = out_dir
        for part in meta.pkg_parts:
            partial /= part
            (partial / "__init__.py").touch(exist_ok=True)

        imp_lines, alias_map = _py_imports(meta, classes, enums)
        lines = imp_lines
        lines += ["", "@dataclass"]
        bases = [alias_map.get(b, b) for b in meta.bases] or ["CIMObject"]
        if meta.is_abstract and "ABC" not in bases:
            bases.append("ABC")
        lines.append(f"class {meta.name}({', '.join(bases)}):")
        if meta.doc:
            lines.append(f"    \"\"\"{meta.doc}\"\"\"")
        for a in meta.attrs.values():
            default = ""
            if a.type_.startswith("Optional["):
                default = " = None"
            elif a.type_.startswith("list["):
                default = " = field(default_factory=list)"
            if a.is_ref and not a.type_.startswith("list["):
                lines.append(
                    f"    {a.name}_ref: {a.type_}{default}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
                )
                lines.append(f"    {a.name}_id: str = None")
            else:
                lines.append(
                    f"    {a.name}: {a.type_}{default}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
                )
        if not meta.attrs:
            lines.append("    pass")
        (pkg_dir / f"{meta.name}.py").write_text("\n".join(lines) + "\n", encoding="utf-8")
        cnt += 1
    return cnt

# ────────────────────────────────────────────────────────────────
#  PUBLIC API
# ────────────────────────────────────────────────────────────────

def generate_dataclasses(xmi: str | Path, output_dir: str | Path) -> int:
    """Parse *xmi* and write dataclass modules into *output_dir*.

    Returns the number of generated classes.
    """
    tree = _load_xmi(Path(xmi))
    classes, enums, _ = _parse_xmi(tree)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "__init__.py").touch(exist_ok=True)

    # upiši bazu
    (out_dir / "base.py").write_text(_BASE_SRC, encoding="utf-8")
    n_enum = _write_enums(enums, out_dir)
    n_cls = _write_classes(classes, enums, out_dir)
    print(f"✅ Generisano {n_enum} enumeracija i {n_cls} klasa.")
    return n_enum + n_cls


# ────────────────────────────────────────────────────────────────
#  Minimalni runtime (neizmenjen)
# ────────────────────────────────────────────────────────────────

_BASE_SRC = """from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import List, Optional

from rdflib import Graph, Literal, Namespace, RDF, URIRef

CIM = Namespace('http://iec.ch/TC57/2013/CIM-schema-cim#')

@dataclass
class CIMObject:
    rdf_id: str

    _cim_type: str = 'CIMObject'

    def to_rdf(self, g: Graph) -> URIRef:
        subj = URIRef(f'#{self.rdf_id}')
        g.add((subj, RDF.type, CIM[self._cim_type]))
        g.add((subj, CIM['IdentifiedObject.mRID'], Literal(self.rdf_id)))
        for f in fields(self):
            if f.name == 'rdf_id':
                continue
            pred = CIM[f.metadata.get('cim', f.name).split('.')[-1]]
            val = getattr(self, f.name)
            if val is None:
                continue
            if isinstance(val, list):
                for v in val:
                    _add(subj, pred, v, g)
            else:
                _add(subj, pred, val, g)
        return subj

def _add(s: URIRef, p: URIRef, v, g: Graph):
    if hasattr(v, 'rdf_id'):
        g.add((s, p, URIRef(f'#{v.rdf_id}')))
    else:
        g.add((s, p, Literal(v)))
"""

# ────────────────────────────────────────────────────────────────
#  CLI
# ────────────────────────────────────────────────────────────────

def _cli():
    """Parse command line arguments and trigger dataclass generation."""
    ap = argparse.ArgumentParser(
        description=
        "Generate CGMES dataclasses from XMI. Definitions sharing an XMI id "
        "or identical package path are merged, so classes like TopologicalNode "
        "may accumulate associations from multiple profiles. Dependency links "
        "add extra base classes. If a dependency target is missing, the script "
        "searches for a class with the same GUIDBasedOn value."
    )
    ap.add_argument("xmi")
    ap.add_argument("-o", "--output", required=True)
    args = ap.parse_args()
    generate_dataclasses(args.xmi, args.output)


if __name__ == "__main__":
    # _cli()
    generate_dataclasses("cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml", "generated")

