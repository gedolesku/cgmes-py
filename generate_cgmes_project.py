#!/usr/bin/env python3
"""Generate Python dataclasses from a CGMES XMI file (ENTSO‑E 2.4.x)
===================================================================

Možeš ga **pokrenuti na dva načina**:

1. **Iz komandne linije** (kao ranije):

    ```bash
    python generate_dataclasses.py ENTSOE_CGMES_v2.4.15_7Aug2014_XMI.zip -o cgmes_py
    ```

2. **Direktno iz koda** (bez `argparse`):

    ```python
    from generate_dataclasses import generate_dataclasses

    generate_dataclasses("ENTSOE_CGMES_v2.4.15_7Aug2014_XMI.zip", output_dir="cgmes_py")
    ```

Skripta će:
    • Pronaći i otvoriti XMI (direktno ili iz ZIP‑a)
    • Parsirati UML pakete, klase, atribute i nasleđivanje
    • Kreirati zaseban `@dataclass` fajl za svaku CIM klasu, zadržavajući CamelCase nazive
    • Rekonstruisati paketnu hijerarhiju i dodati prazan `__init__.py` u svaki paket

Rezultat je spreman za **Pylance/Pyright** – IntelliSense radi odmah.
"""

from __future__ import annotations

import argparse
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from lxml import etree

# ────────────────────────────────────────────────────────────────
# Konstante i mapiranja
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
}

# ────────────────────────────────────────────────────────────────
# Interni modeli
# ────────────────────────────────────────────────────────────────

@dataclass
class Attribute:
    name: str
    type_: str
    multiplicity: str = "1"  # "1", "0..1", "0..*", "1..*", ...


@dataclass
class ClassMeta:
    name: str
    attrs: List[Attribute]
    parent: str | None
    pkg_parts: Tuple[str, ...]  # npr. ("Equipment", "Core")


# ────────────────────────────────────────────────────────────────
# Parsiranje XMI‑ja
# ────────────────────────────────────────────────────────────────

def _parse_xmi(tree: etree._ElementTree) -> Dict[str, ClassMeta]:
    """Vrati mapu *ime‑klase → ClassMeta* iz XMI stabla."""

    root = tree.getroot()
    id_index = {e.get(f"{{{XMI_NS}}}id"): e for e in root.iter() if e.get(f"{{{XMI_NS}}}id")}

    primitive_ids = {
        e.get(f"{{{XMI_NS}}}id"): PRIMITIVE_MAP[e.get("name")]
        for e in root.xpath(".//uml:PrimitiveType", namespaces=NSMAP)
        if e.get("name") in PRIMITIVE_MAP
    }

    classes: Dict[str, ClassMeta] = {}

    def walk_package(elem, pkg_path: List[str]):
        for child in elem.xpath("./uml:packagedElement", namespaces=NSMAP):
            xmi_type = child.get(f"{{{XMI_NS}}}type")

            if xmi_type == "uml:Package":
                walk_package(child, pkg_path + [child.get("name")])
                continue

            if xmi_type != "uml:Class":
                continue

            cname = child.get("name")
            attrs: List[Attribute] = []

            for prop in child.xpath("./uml:ownedAttribute", namespaces=NSMAP):
                attr_name = prop.get("name")
                type_ref = prop.get("type")

                lower = prop.get("lowerValue") or "1"
                upper = prop.get("upperValue") or "1"
                multiplicity = f"{lower}..{upper}" if lower != upper else lower

                ptype = "str"  # podrazumevano
                if type_ref:
                    if type_ref in primitive_ids:
                        ptype = primitive_ids[type_ref]
                    else:
                        t_elem = id_index.get(type_ref)
                        if t_elem is not None:
                            ptype = t_elem.get("name") or "str"

                if multiplicity not in ("0", "1"):
                    ptype = f"list[{ptype}]"

                attrs.append(Attribute(attr_name, ptype, multiplicity))

            parent = None
            gen = child.find("uml:generalization", namespaces=NSMAP)
            if gen is not None and (target := gen.get("general")):
                if (t_elem := id_index.get(target)) is not None:
                    parent = t_elem.get("name")

            classes[cname] = ClassMeta(cname, attrs, parent, tuple(pkg_path))

    walk_package(root, [])
    return classes


# ────────────────────────────────────────────────────────────────
# Generisanje Python fajlova
# ────────────────────────────────────────────────────────────────

def _write_classes(classes: Dict[str, ClassMeta], out_dir: Path) -> int:
    """Materijalizuj svaki *ClassMeta* u poseban `.py` fajl i vrati broj generisanih klasa."""

    count = 0
    for meta in classes.values():
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)

        # __init__.py na svakom nivou
        partial = out_dir
        for part in meta.pkg_parts:
            partial /= part
            (partial / "__init__.py").touch(exist_ok=True)

        # Importi za reference na druge klase iz istog paketa
        imports = set()
        for attr in meta.attrs:
            base = re.sub(r"^list\[(.*)\]$", r"\1", attr.type_)
            if base in classes and base != meta.name:
                imports.add(f"from .{base} import {base}")
        if meta.parent and meta.parent in classes:
            imports.add(f"from .{meta.parent} import {meta.parent}")

        lines: List[str] = [
            "from __future__ import annotations",
            "from dataclasses import dataclass",
            "from typing import Optional, List",
            *sorted(imports),
            "",
            "@dataclass",
            f"class {meta.name}({meta.parent or 'object'}):",
        ]

        if not meta.attrs:
            lines.append("    pass")
        else:
            for attr in meta.attrs:
                ann = attr.type_
                if attr.multiplicity.startswith("0") and not ann.startswith("list["):
                    ann = f"Optional[{ann}]"
                default = " = None" if ann.startswith("Optional[") else ""
                lines.append(f"    {attr.name}: {ann}{default}")

        (pkg_dir / f"{meta.name}.py").write_text("\n".join(lines), encoding="utf‑8")
        count += 1

    return count


# ────────────────────────────────────────────────────────────────
# Javni API
# ────────────────────────────────────────────────────────────────

def generate_dataclasses(xmi_source: str | Path, output_dir: str | Path) -> int:
    """Generiši dataclass fajlove i vrati broj kreiranih klasa.

    Parameters
    ----------
    xmi_source : str | Path
        Putanja do `.xmi` fajla ili `.zip` arhive u kojoj se nalazi `.xmi`.
    output_dir : str | Path
        Direktorijum u koji će biti upisani generisani paketi/klase.
    """

    src = Path(xmi_source)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Učitaj XMI (direktno ili iz ZIP‑a)
    if src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src, "r") as zf:
            xmi_names = [n for n in zf.namelist() if n.lower().endswith(".xmi")]
            if not xmi_names:
                raise RuntimeError("ZIP ne sadrži .xmi fajl!")
            data = zf.read(xmi_names[0])
            tree = etree.ElementTree(etree.fromstring(data))
    else:
        tree = etree.parse(str(src))

    classes = _parse_xmi(tree)
    count = _write_classes(classes, out_dir)
    print(f"✅ Generisano {count} klasa u '{out_dir}'.")
    return count


# ────────────────────────────────────────────────────────────────
# CLI omotač (i dalje postoji za backward compat.)
# ────────────────────────────────────────────────────────────────

def _cli() -> None:
    parser = argparse.ArgumentParser(description="Generate Python dataclasses from a CGMES 2.4 XMI file")
    parser.add_argument("xmi_source", help="Path to .xmi file or .zip containing one")
    parser.add_argument("--output", "-o", required=True, help="Output directory for generated code")
    args = parser.parse_args()
    generate_dataclasses(args.xmi_source, args.output)


if __name__ == "__main__":
    #_cli()
  generate_dataclasses(r"cgmes-models\v24\ENTSOE_CGMES_v2.4.14_28May2014.xml", output_dir="cgmes_py")
