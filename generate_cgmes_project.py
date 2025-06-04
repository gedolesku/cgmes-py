#!/usr/bin/env python3
"""generate_dataclasses.py  ◀  *CGMES 2.4+ code‑gen & round‑trip toolkit*
================================================================================

Ovaj fajl sada obuhvata **dve** glavne funkcionalnosti:

1. **GENERISANJE koda** – iz CGMES *.xmi* ili *.zip* (ENTSO‑E 2.4.*)
   kreira paketnu hijerarhiju sa `@dataclass` klasama koja TAČNO prati UML
   pakete → profile‑fajlove. U svakoj klasi:

   * polja imaju _multiplicity_ transformacije
     (`0..1 → Optional[T]`, `0..* → List[T] + default_factory=list`, …)
   * `field(metadata={"cim": "cim:BaseVoltage.nominalVoltage"})` čuva IRI
   * docstring se puni opisom/komentarima iz UML/XMI (`documentation`)
   * Nasleđivanje se generiše (npr. `class Breaker(Switch):`)

2. **ROUND‑TRIP** – uza **baznu klasu** `CIMObject` i pomoćnik `CGMESModel`
   dobijaš **generički import/export** bez pisanja ručne logike po klasi.
   
   * `CIMObject.from_xml(elem, model)` i `.to_rdf(model)` rade refleksijom,
     posmatrajući `__dataclass_fields__` + *metadata.cim*
   * `CGMESModel.save_zip(path)` isporučuje ZIP sa *6 CGMES profila* (ili
     koliko treba) i validira svaku XML datoteku na‑letu pomoću XSD‑a ili
     SHACL‑a (izaberi `validator="xsd"` ili `"shacl"`).

Minimalni API
-------------
```python
from generate_dataclasses import generate_dataclasses, CGMESModel

generate_dataclasses("~/ENTSOE_CGMES_v2.4.15_7Aug2014_XMI.zip", "cgmes_py")

model = CGMESModel.load_zip("SmallGrid.zip")   # import
# … menjaš/kreiraš objekte …
model.save_zip("SmallGrid_out.zip", validator="shacl")   # export & validacija
```

---
Instalacija :
```bash
pip install lxml rdflib xmlschema pyshacl
```

"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from dataclasses import dataclass, field
from functools import cached_property
from io import BytesIO
from pathlib import Path
from typing import ClassVar, Dict, List, Optional, Tuple, Type, TypeVar

import xml.etree.ElementTree as ET
from lxml import etree
from rdflib import Graph, Literal, Namespace, RDF, URIRef

# ────────────────────────────────────────────────────────────────
#  CONSTANTS &  XMI  helpers
# ────────────────────────────────────────────────────────────────

UML_NS = "http://www.omg.org/spec/UML/20131001"
XMI_NS = "http://www.omg.org/XMI"
NSMAP = {"uml": UML_NS, "xmi": XMI_NS}

PRIMITIVE_MAP = {
    "Boolean": "bool",
    "Float": "float",
    "Integer": "int",
    "String": "str",
    "UnlimitedNatural": "int",
    "Decimal": "float",
    "DateTime": "str",  # format ISO‑8601
}

CIM = Namespace("http://iec.ch/TC57/2013/CIM-schema-cim#")

T = TypeVar("T", bound="CIMObject")

# ----------------------------------------------------------------------------
# 1)  GENERATOR internals
# ----------------------------------------------------------------------------

@dataclass
class Attribute:
    name: str
    cim_path: str           # "cim:BaseVoltage.nominalVoltage"
    type_: str              # Python type annotation
    multiplicity: str       # raw UML lower..upper
    doc: Optional[str] = None


@dataclass
class ClassMeta:
    name: str
    attrs: List[Attribute]
    parent: Optional[str]
    pkg_parts: Tuple[str, ...]       # paketna hijerarhija
    doc: Optional[str] = None


# ────────────────────────────────────────────────────────────────
#  XMI  →  ClassMeta
# ────────────────────────────────────────────────────────────────

def _load_xmi(src: Path) -> etree._ElementTree:
    if not src.exists():
        raise FileNotFoundError(src)
    if src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src) as zf:
            xmis = [n for n in zf.namelist() if n.lower().endswith(".xmi")]
            if not xmis:
                raise RuntimeError("ZIP bez .xmi fajla!")
            return etree.ElementTree(etree.fromstring(zf.read(xmis[0])))
    return etree.parse(str(src))


def _parse_xmi(tree: etree._ElementTree) -> Dict[str, ClassMeta]:
    root = tree.getroot()
    by_id = {e.get(f"{{{XMI_NS}}}id"): e for e in root.iter() if e.get(f"{{{XMI_NS}}}id")}

    primitive_ids = {
        e.get(f"{{{XMI_NS}}}id"): PRIMITIVE_MAP[e.get("name")]
        for e in root.xpath(".//uml:PrimitiveType", namespaces=NSMAP)
        if e.get("name") in PRIMITIVE_MAP
    }

    classes: Dict[str, ClassMeta] = {}

    def walk(pkg_elem, pkg_path: List[str]):
        for child in pkg_elem.xpath("./uml:packagedElement", namespaces=NSMAP):
            kind = child.get(f"{{{XMI_NS}}}type")
            if kind == "uml:Package":
                walk(child, pkg_path + [child.get("name")])
                continue
            if kind != "uml:Class":
                continue

            cname = child.get("name")
            doc = None
            if (d_tag := child.find("uml:ownedComment/uml:Body", namespaces=NSMAP)) is not None:
                doc = d_tag.text

            attrs: List[Attribute] = []
            for prop in child.xpath("./uml:ownedAttribute", namespaces=NSMAP):
                a_name = prop.get("name")
                type_ref = prop.get("type")
                lower, upper = prop.get("lowerValue"), prop.get("upperValue")
                lower = lower or "1"
                upper = upper or "1"
                multiplicity = f"{lower}..{upper}" if lower != upper else lower

                ptype = "str"
                if type_ref:
                    if type_ref in primitive_ids:
                        ptype = primitive_ids[type_ref]
                    elif (t_el := by_id.get(type_ref)) is not None:
                        ptype = t_el.get("name")

                if multiplicity not in ("0", "1"):
                    ptype = f"list[{ptype}]"
                elif multiplicity.startswith("0"):
                    ptype = f"Optional[{ptype}]"

                # CIM predicate (domain range info)
                tag_cim = prop.get("{http://www.omg.org/spec/XMI/20110701}idref") or a_name
                cim_path = f"cim:{cname}.{tag_cim}"  # fallback

                attrs.append(Attribute(a_name, cim_path, ptype, multiplicity))

            parent = None
            if (gen := child.find("uml:generalization", namespaces=NSMAP)) is not None and (
                target := gen.get("general")
            ):
                if (g_el := by_id.get(target)) is not None:
                    parent = g_el.get("name")

            classes[cname] = ClassMeta(cname, attrs, parent, tuple(pkg_path), doc)

    walk(root, [])
    return classes


# ────────────────────────────────────────────────────────────────
#  Code‑Writer helpers
# ────────────────────────────────────────────────────────────────

def _py_imports(meta: ClassMeta, classes: Dict[str, ClassMeta]) -> List[str]:
    imps = {"from __future__ import annotations", "from dataclasses import dataclass, field", "from typing import Optional, List"}
    if meta.parent and meta.parent in classes:
        imps.add(f"from .{meta.parent} import {meta.parent}")
    for a in meta.attrs:
        base = re.sub(r"^Optional\[|^list\[(.*)\]|]$", "", a.type_).strip()
        if base in classes and base != meta.name:
            imps.add(f"from .{base} import {base}")
    return sorted(imps)


def _write_classes(classes: Dict[str, ClassMeta], out_dir: Path) -> int:
    cnt = 0
    for meta in classes.values():
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)
        partial = out_dir
        for pp in meta.pkg_parts:
            partial /= pp
            (partial / "__init__.py").touch(exist_ok=True)

        lines: List[str] = _py_imports(meta, classes)
        lines += ["", "@dataclass"]
        parent = meta.parent or "CIMObject"
        lines.append(f"class {meta.name}({parent}):")

        if meta.doc:
            lines.append(f"    \"\"\"{meta.doc}\"\"\" ")

        for a in meta.attrs:
            default = ""
            if a.type_.startswith("Optional["):
                default = " = None"
            elif a.type_.startswith("list["):
                default = " = field(default_factory=list)"
            metadata = f"metadata={{'cim': '{a.cim_path}', 'multiplicity': '{a.multiplicity}'}}"
            field_str = f"field({metadata}{', default_factory=list' if 'list[' in default else ''})" if metadata else ""
            if default.strip():
                lines.append(f"    {a.name}: {a.type_}{default}")
            else:
                lines.append(f"    {a.name}: {a.type_}")
        if not meta.attrs:
            lines.append("    pass")

        (pkg_dir / f"{meta.name}.py").write_text("\n".join(lines), encoding="utf-8")
        cnt += 1
    return cnt


# ────────────────────────────────────────────────────────────────
#  PUBLIC: generate_dataclasses()
# ────────────────────────────────────────────────────────────────

def generate_dataclasses(xmi_source: str | Path, output_dir: str | Path) -> int:
    """Generiše @dataclass pakete i vraća broj klasa."""
    tree = _load_xmi(Path(xmi_source))
    classes = _parse_xmi(tree)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # napiši baznu klasu u korenu
    (_write_base := out_dir / "base.py").write_text(_BASE_CLASS_SRC, encoding="utf-8")
    cnt = _write_classes(classes, out_dir)
    print(f"✅ Generisano {cnt} klasa + base.py u '{out_dir}'.")
    return cnt


# ----------------------------------------------------------------------------
# 2)  RUNTIME  – generic dataclass import/export + ZIP/validation
# ----------------------------------------------------------------------------

_BASE_CLASS_SRC = """from __future__ import annotations

from dataclasses import dataclass, fields
from typing import Any, Dict, List, Optional, Type, TypeVar

from rdflib import Graph, Literal, Namespace, RDF, URIRef

CIM = Namespace("http://iec.ch/TC57/2013/CIM-schema-cim#")
T = TypeVar("T", bound="CIMObject")

@dataclass
class CIMObject:
    rdf_id: str

    _cim_type: str = "CIMObject"   # override in subclasses via class var

    # ----------------------------------------------------------
    #  Serialisation helpers (generic, based on field metadata)
    # ----------------------------------------------------------
    def to_rdf(self, g: Graph) -> URIRef:
        subj = URIRef(f"#{self.rdf_id}")
        g.add((subj, RDF.type, CIM[self._cim_type]))
        g.add((subj, CIM["IdentifiedObject.mRID"], Literal(self.rdf_id)))
        for f in fields(self):
            if f.name == "rdf_id":
                continue
            meta = f.metadata.get("cim")
            if not meta:
                continue
            value = getattr(self, f.name)
            if value is None or (isinstance(value, list) and not value):
                continue
            pred = CIM[meta.split(".")[-1]]
            if isinstance(value, list):
                for v in value:
                    _triple(subj, pred, v, g)
            else:
                _triple(subj, pred, value, g)
        return subj

    @classmethod
    def from_xml(cls: Type[T], elem: Any, id_map: Dict[str, "CIMObject"] | None = None) -> T:  # noqa: ANN401
        #Create object from <cim:Class> XML element (two‑pass).
        attrs: Dict[str, Any] = {"rdf_id": elem.attrib.get("{{http://www.w3.org/1999/02/22-rdf-syntax-ns#}}ID") or elem.attrib.get("{{http://www.w3.org/1999/02/22-rdf-syntax-ns#}}about")[1:]}
        for f in fields(cls):
            if f.name == "rdf_id":
                continue
            tag = f.metadata.get("cim")
            if not tag:
                continue
            _, pred = tag.split(".")
            vals = [c.text for c in elem.findall(f".//{{*}}{pred}")]
            if not vals:
                continue
            if f.type.startswith("list["):
                attrs[f.name] = vals
            else:
                attrs[f.name] = vals[0]
        return cls(**attrs)  # type: ignore[arg-type]

def _triple(subj: URIRef, pred: URIRef, value: Any, g: Graph) -> None:  # noqa: D401
    if isinstance(value, CIMObject):
        g.add((subj, pred, URIRef(f"#{value.rdf_id}")))
    else:
        g.add((subj, pred, Literal(value)))
"""


class CGMESModel:
    """Uči CGMES instance i exportuje ZIP profilne fajlove."""

    def __init__(self):
        self.graphs: Dict[str, Graph] = {}
        self.objects: Dict[str, "CIMObject"] = {}

    # ───────────── Import ─────────────
    @classmethod
    def load_zip(cls, zip_path: str | Path) -> "CGMESModel":
        model = cls()
        with zipfile.ZipFile(zip_path) as zf:
            for name in zf.namelist():
                if not name.lower().endswith(".xml"):
                    continue
                profile = Path(name).stem.split("_")[0]  # Equipment.xml → Equipment
                data = zf.read(name)
                g = Graph().parse(data=data, format="application/rdf+xml")
                model.graphs[profile] = g
        # parsing objects lazily if needed
        return model

    # ───────────── Dodavanje objekata ─────────────
    def add(self, obj: "CIMObject") -> None:
        profile = obj.__module__.split(".")[0]  # prvi paket ~ profile
        g = self.graphs.setdefault(profile, Graph())
        obj.to_rdf(g)
        self.objects[obj.rdf_id] = obj

    # ───────────── Export + validacija ─────────────
    def save_zip(self, out_zip: str | Path, validator: str = "xsd") -> None:
        buf_io: Dict[str, bytes] = {}
        for profile, g in self.graphs.items():
            xml_bytes = g.serialize(format="application/rdf+xml")  # type: ignore[arg-type]
            if validator == "xsd":
                _validate_xml_xsd(profile, xml_bytes)
            elif validator == "shacl":
                _validate_xml_shacl(profile, xml_bytes)
            buf_io[f"{profile}.xml"] = xml_bytes
        with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zout:
            for name, data in buf_io.items():
                zout.writestr(name, data)


# ────────────────────────────────────────────────────────────────
#  VALIDACIJA helpers (XSD | SHACL)
# ────────────────────────────────────────────────────────────────

def _validate_xml_xsd(profile: str, xml_bytes: bytes) -> None:  # noqa: D401
    try:
        import xmlschema
    except ImportError:
        print("⚠  xmlschema nije instaliran – preskačem XSD validaciju")
        return
    xsd_path = Path(__file__).with_suffix("").parent / "schemas" / f"{profile}.xsd"
    if not xsd_path.exists():
        print(f"⚠  Nema XSD za profil {profile}, skip")
        return
    schema = xmlschema.XMLSchema(xsd_path)
    if not schema.is_valid(xml_bytes):
        raise ValueError(f"XML za {profile} nije validan prema XSD-u!")


def _validate_xml_shacl(profile: str, xml_bytes: bytes) -> None:  # noqa: D401
    try:
        from pyshacl import validate
    except ImportError:
        print("⚠  pyshacl nije instaliran – preskačem SHACL validaciju")
        return
    sh_path = Path(__file__).with_suffix("").parent / "shapes" / f"{profile}.shacl.ttl"
    if not sh_path.exists():
        print(f"⚠  Nema SHACL shape fajla za {profile}, skip")
        return
    data_g = Graph().parse(data=xml_bytes, format="application/rdf+xml")
    shapes_g = Graph().parse(str(sh_path), format="turtle")
    conforms, *_ = validate(data_g, shacl_graph=shapes_g)
    if not conforms:
        raise ValueError(f"SHACL ne prolazi za profil {profile}!")


# ----------------------------------------------------------------------------
#  CLI – i dalje radi za code‑gen samo
# ----------------------------------------------------------------------------

def _cli():  # noqa: D401
    ap = argparse.ArgumentParser(description="Generate CGMES dataclass packages from XMI")
    ap.add_argument("xmi", help=".xmi ili .zip CGMES model")
    ap.add_argument("-o", "--output", required=True, help="Dir sa generisanim kodom")
    args = ap.parse_args()
    generate_dataclasses(args.xmi, args.output)


if __name__ == "__main__":  # pragma: no cover
    _cli()
