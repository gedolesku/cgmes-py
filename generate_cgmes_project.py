#!/usr/bin/env python3
"""generate_dataclasses.py  ◀  CGMES 2.4+ **code‑gen & round‑trip toolkit**
================================================================================

### Šta je novo?  (2025‑06‑04)
* **Podržani su i atributi iz `uml:Association` krajeva** (`ownedEnd`) – pa
  reference poput `DiagramObjectPoint.DiagramObject` više NE izostaju.
* Multiplicitete se čitaju i kada su definisani kao pod‑elementi
  `<uml:lowerValue value="0"/>`, `<uml:upperValue value="*"/>`.
* Fiksirano mapiranje `*` → `list[T]`, a `0|0..1` → `Optional[T]`.
* Generator sada sprečava duplikate atributa (npr. ako postoji i *ownedAttr*
  i *association end* istog imena).

---
Minimalni primer:
```bash
python generate_dataclasses.py ENTSOE_CGMES_v2.4.15_7Aug2014_XMI.zip -o cgmes_py
```
Na izlazu dobijaš hijerarhiju paketa + `base.py` (sa `CIMObject`).
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from lxml import etree
from rdflib import Graph, Literal, Namespace, RDF, URIRef

# ────────────────────────────────────────────────────────────────
#  KONSTANTE
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
#  METAPODACI
# ────────────────────────────────────────────────────────────────

@dataclass
class Attribute:
    name: str
    cim_path: str
    type_: str
    multiplicity: str
    doc: Optional[str] = None


@dataclass
class ClassMeta:
    name: str
    attrs: Dict[str, Attribute]  # key = attribute name (dedup)
    parent: Optional[str]
    pkg_parts: Tuple[str, ...]
    doc: Optional[str] = None


# ────────────────────────────────────────────────────────────────
#  XMI parsiranje
# ────────────────────────────────────────────────────────────────

def _load_xmi(src: Path) -> etree._ElementTree:
    if not src.exists():
        raise FileNotFoundError(src)
    if src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src) as zf:
            xmis = [n for n in zf.namelist() if n.lower().endswith(".xmi") or n.lower().endswith(".xml")]
            if not xmis:
                raise RuntimeError("ZIP bez .xmi/.xml fajla!")
            return etree.ElementTree(etree.fromstring(zf.read(xmis[0])))
    return etree.parse(str(src))


def _mult_from_elem(elem: etree._Element) -> Tuple[str, str]:
    """Vrati (lower, upper) kao stringove."""
    lower = elem.get("lower") or elem.get("lowerValue")
    upper = elem.get("upper") or elem.get("upperValue")
    if lower is None:
        if (lv := elem.find("uml:lowerValue", namespaces=NSMAP)) is not None:
            lower = lv.get("value") or "1"
    if upper is None:
        if (uv := elem.find("uml:upperValue", namespaces=NSMAP)) is not None:
            upper = uv.get("value") or "1"
    return (lower or "1", upper or "1")


def _ptype_from_multiplicity(base: str, lower: str, upper: str) -> str:
    if upper == "*" or ".." in f"{lower}..{upper}" and (upper == "*" or int(upper) > 1):
        return f"list[{base}]"
    if lower == "0":
        return f"Optional[{base}]"
    return base


def _parse_xmi(tree: etree._ElementTree) -> Dict[str, ClassMeta]:
    root = tree.getroot()
    by_id = {e.get(f"{{{XMI_NS}}}id"): e for e in root.iter() if e.get(f"{{{XMI_NS}}}id")}

    primitive_ids = {
        e.get(f"{{{XMI_NS}}}id"): PRIMITIVE_MAP[e.get("name")]
        for e in root.xpath(".//packagedElement[@xmi:type='uml:PrimitiveType']", namespaces=NSMAP)
        if e.get("name") in PRIMITIVE_MAP
    }

    classes: Dict[str, ClassMeta] = {}

    def walk(pkg_elem, pkg_path: List[str]):
        for child in pkg_elem.xpath("./packagedElement"):
            kind = child.get(f"{{{XMI_NS}}}type")
            if kind == "uml:Package":
                walk(child, pkg_path + [child.get("name")])
                continue
            if kind != "uml:Class":
                continue

            cname = child.get("name")
            doc = None
            if (c_doc := child.find("uml:ownedComment/uml:Body", namespaces=NSMAP)) is not None:
                doc = c_doc.text

            class_meta = ClassMeta(cname, {}, None, tuple(pkg_path), doc)
            classes[cname] = class_meta

            for prop in child.xpath("./uml:ownedAttribute", namespaces=NSMAP):
                a_name = prop.get("name")
                type_ref = prop.get("type")
                lower, upper = _mult_from_elem(prop)

                base_type = "str"
                if type_ref:
                    base_type = primitive_ids.get(type_ref) or by_id.get(type_ref).get("name")

                ptype = _ptype_from_multiplicity(base_type, lower, upper)
                mult_raw = f"{lower}..{upper}" if lower != upper else lower
                tag_cim = prop.get("{http://www.omg.org/spec/XMI/20110701}idref") or a_name
                cim_path = f"cim:{cname}.{tag_cim}"

                class_meta.attrs[a_name] = Attribute(a_name, cim_path, ptype, mult_raw)

            if (gen := child.find("uml:generalization", namespaces=NSMAP)) is not None and (
                tgt := gen.get("general")
            ):
                if (t_el := by_id.get(tgt)) is not None:
                    class_meta.parent = t_el.get("name")

    walk(root, [])

    for assoc in root.xpath(".//packagedElement[@xmi:type='uml:Association']", namespaces=NSMAP):
        ends = assoc.xpath("./uml:ownedEnd", namespaces=NSMAP)
        if len(ends) < 2:
            continue
        for end in ends:
            owner_id = end.get("type")
            if owner_id not in by_id:
                continue
            owner_name = by_id[owner_id].get("name")
            target_id = None
            for other in ends:
                if other is not end and other.get("type"):
                    target_id = other.get("type")
                    break
            if not target_id or target_id not in by_id:
                continue
            target_name = by_id[target_id].get("name")
            a_name = end.get("name") or target_name
            lower, upper = _mult_from_elem(end)
            ptype = _ptype_from_multiplicity(target_name, lower, upper)
            mult_raw = f"{lower}..{upper}" if lower != upper else lower
            cim_path = f"cim:{owner_name}.{a_name}"
            meta = classes[owner_name]
            if a_name not in meta.attrs:
                meta.attrs[a_name] = Attribute(a_name, cim_path, ptype, mult_raw)

    return classes


# ────────────────────────────────────────────────────────────────
#  Code writer
# ────────────────────────────────────────────────────────────────

def _py_imports(meta: ClassMeta, classes: Dict[str, ClassMeta]) -> List[str]:
    imps = {
        "from __future__ import annotations",
        "from dataclasses import dataclass, field",
        "from typing import Optional, List",
    }
    if meta.parent and meta.parent in classes:
        imps.add(f"from .{meta.parent} import {meta.parent}")
    for a in meta.attrs.values():
        base = re.sub(r"^Optional\[|\]$", "", a.type_)
        base = re.sub(r"^list\[(.*)\]$", r"\1", base)
        if base in classes and base != meta.name:
            imps.add(f"from .{base} import {base}")
    return sorted(imps)


def _write_classes(classes: Dict[str, ClassMeta], out_dir: Path) -> int:
    cnt = 0
    for meta in classes.values():
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)
        # ensure __init__.py
        partial = out_dir
        for part in meta.pkg_parts:
            partial /= part
            (partial / "__init__.py").touch(exist_ok=True)

        lines = _py_imports(meta, classes)
        lines += ["", "@dataclass"]
        parent = meta.parent or "CIMObject"
        lines.append(f"class {meta.name}({parent}):")
        if meta.doc:
            lines.append(f"    \"\"\"{meta.doc}\"\"\"")
        for a in meta.attrs.values():
            default = ""
            if a.type_.startswith("Optional["):
                default = " = None"
            elif a.type_.startswith("list["):
                default = " = field(default_factory=list)"
            lines.append(
                f"    {a.name}: {a.type_}{default}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
            )
        if not meta.attrs:
            lines.append("    pass")
        (pkg_dir / f"{meta.name}.py").write_text("\n".join(lines), encoding="utf-8")
        cnt += 1
    return cnt


# ────────────────────────────────────────────────────────────────
#  PUBLIC API
# ────────────────────────────────────────────────────────────────

def generate_dataclasses(xmi: str | Path, output_dir: str | Path) -> int:
    tree = _load_xmi(Path(xmi))
    classes = _parse_xmi(tree)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # upiši bazu
    (out_dir / "base.py").write_text(_BASE_SRC, encoding="utf-8")
    n = _write_classes(classes, out_dir)
    print(f"✅ Generisano {n} klasa.")
    return n


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
    ap = argparse.ArgumentParser(description="Generate CGMES dataclasses from XMI")
    ap.add_argument("xmi")
    ap.add_argument("-o", "--output", required=True)
    args = ap.parse_args()
    generate_dataclasses(args.xmi, args.output)


if __name__ == "__main__":
    _cli()

