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


@dataclass
class ClassMeta:
    name: str
    attrs: Dict[str, Attribute]
    parent: Optional[str]
    pkg_parts: Tuple[str, ...]

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


def _ptype(base: str, lower: str, upper: str) -> str:
    if upper == "*" or (upper.isdigit() and int(upper) > 1):
        return f"list[{base}]"
    if lower == "0":
        return f"Optional[{base}]"
    return base

# ────────────────────────────────────────────────────────────────
#  Parsiranje
# ────────────────────────────────────────────────────────────────

def _parse_xmi(tree: etree._ElementTree) -> Dict[str, ClassMeta]:
    root = tree.getroot()
    by_id = {e.get(f"{{{XMI_NS}}}id"): e for e in root.iter() if e.get(f"{{{XMI_NS}}}id")}

    prim_elems = root.xpath(".//packagedElement[@xmi:type='uml:PrimitiveType']", namespaces=NSMAP)
    primitive_ids = {e.get(f"{{{XMI_NS}}}id"): PRIMITIVE_MAP.get(e.get("name")) for e in prim_elems}

    classes: Dict[str, ClassMeta] = {}

    def walk(elem, pkg_path: List[str]):
        for child in elem.xpath("./packagedElement"):
            kind = child.get(f"{{{XMI_NS}}}type")
            if kind == "uml:Package":
                walk(child, pkg_path + [child.get("name")])
                continue
            if kind != "uml:Class":
                continue
            cname = child.get("name")
            if DEBUG:
                print("🔍 Klasa", cname)
            meta = ClassMeta(cname, {}, None, tuple(pkg_path))
            classes[cname] = meta

            # ownedAttribute
            for prop in child.xpath("./ownedAttribute"):
                a_name = prop.get("name")
                type_ref = prop.get("type")
                lower, upper = _mult_from_elem(prop)
                base_type = primitive_ids.get(type_ref) or (by_id.get(type_ref).get("name") if type_ref in by_id else "str")
                meta.attrs[a_name] = Attribute(
                    a_name,
                    f"cim:{cname}.{a_name}",
                    _ptype(base_type, lower, upper),
                    f"{lower}..{upper}" if lower != upper else lower,
                )

            # generalization
            gen = child.find("generalization")
            if gen is not None and (gid := gen.get("general")) and gid in by_id:
                meta.parent = by_id[gid].get("name")

    # start from each uml:Model
    for model in root.xpath(".//uml:Model", namespaces=NSMAP):
        walk(model, [])

    # associations
    for assoc in root.xpath(".//packagedElement[@xmi:type='uml:Association']", namespaces=NSMAP):
        ends = assoc.xpath("./ownedEnd")
        if len(ends) < 2:
            continue
        for end in ends:
            owner_id = end.get("type")
            target_id = next((e.get("type") for e in ends if e is not end and e.get("type")), None)
            if owner_id in by_id and target_id in by_id:
                owner, target = by_id[owner_id].get("name"), by_id[target_id].get("name")
                lower, upper = _mult_from_elem(end)
                classes[owner].attrs.setdefault(
                    end.get("name") or target,
                    Attribute(
                        end.get("name") or target,
                        f"cim:{owner}.{end.get('name') or target}",
                        _ptype(target, lower, upper),
                        f"{lower}..{upper}" if lower != upper else lower,
                    ),
                )

    if DEBUG:
        print("✅ klase:", len(classes), "– prim:", len(primitive_ids))
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


"""
ENTSOE_CGMES_v2.4.15_7Aug2014.xml file chunks
head:
<?xml version="1.0" encoding="windows-1252"?>
<xmi:XMI xmi:version="2.1" xmlns:uml="http://www.omg.org/spec/UML/20090901" xmlns:xmi="http://schema.omg.org/spec/XMI/2.1" xmlns:thecustomprofile="http://www.sparxsystems.com/profiles/thecustomprofile/1.0" xmlns:EPProfile="http://www.sparxsystems.com/profiles/EPProfile/1.0" xmlns:BPMN2.0="http://www.sparxsystems.com/profiles/BPMN2.0/1.5" xmlns:Whiteboard="http://www.sparxsystems.com/profiles/Whiteboard/1.0" xmlns:EAUML="http://www.sparxsystems.com/profiles/EAUML/1.0">
	<xmi:Documentation exporter="Enterprise Architect" exporterVersion="6.5"/>
	<uml:Model xmi:type="uml:Model" name="EA_Model">
		<packagedElement xmi:type="uml:Package" xmi:id="EAPK_8B778221_21A1_4ca2_AE28_2207B96972C0" name="EuropeanStandards">
			<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000000_02F1_4b9d_9F21_AC3391892D86">
				<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_02F1_4b9d_9F21_AC3391892D86" body="choice=simple"/>
			</ownedRule>
			<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000000_0CB5_4dbd_AC4D_C80FE3C83EFD">
				<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_0CB5_4dbd_AC4D_C80FE3C83EFD" body="choice=simple"/>
...

			<packagedElement xmi:type="uml:Package" xmi:id="EAPK_F98BD9A1_D05C_43ed_BB33_B476E4B34588" name="Extension">
				<ownedComment xmi:type="uml:Comment" xmi:id="EAID_D762C349_D2A9_42ce_AAAB_3A6714DC9A9B" body="ENTSOEJunction and Junction class are temporally in the ENTSO-E extension package in case there is a need to use attributes from BoundaryExtension class in the Junction for the Boundary profiles. This is related to the Junction and Boundary profiles issue. Minor change of the CGMES might be agreed during the implementation period when testing different use cases.">
					<annotatedElement xmi:idref="EAID_AFAC6163_E397_49a1_BD3A_E3BF726B0E98"/>
					<annotatedElement xmi:idref="EAID_BE90EE60_8212_44ec_9F4D_775719E80216"/>
				</ownedComment>
				<packagedElement xmi:type="uml:Class" xmi:id="EAID_55F7DB82_8CEA_4d59_B4C6_C5CE92CF3C4E" name="BoundaryExtensions">
					<ownedAttribute xmi:type="uml:Property" xmi:id="EAID_BE2782BE_770A_4d4d_8B4A_3C9AEB84ECAF" name="boundaryPoint">
						<type xmi:idref="EAID_1BD84350_CD0A_4736_A7C4_0017A4F6F699"/>
						<lowerValue xmi:type="uml:LiteralInteger" xmi:id="EAID_LI000001_770A_4d4d_8B4A_3C9AEB84ECAF" value="0"/>
						<upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="EAID_LI000002_770A_4d4d_8B4A_3C9AEB84ECAF" value="1"/>

                        ...

 						<packagedElement xmi:type="uml:Dependency" xmi:id="EAID_24981631_953C_4948_92D8_17EE543BA160" supplier="EAID_82489582_0ECB_4066_970D_A265B1065315" client="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000000_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryDescriptionLength: self.description-&amp;gt;size() &amp;lt;= 256">
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000000_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. Description length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryDescriptionLength: self.description-&amp;gt;size() &amp;lt;= 256"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000001_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. Energy Ident Code length restriction (optional)">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000001_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryEnergyIdentCodeEicLength: self.energyIdentCodeEic = null or self.energyIdentCodeEic-&amp;gt;size() = 16"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000002_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. From End ISO Code length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000002_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryFromEndIsoCodeLength: self.fromEndIsoCode-&amp;gt;size() = 2"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000003_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. From End Name length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000003_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryFromEndNameLength: self.fromEndName-&amp;gt;size() &amp;lt;= 32"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000004_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. From End Name TSO length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000004_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryFromEndNameTsoLength: self.fromEndNameTso-&amp;gt;size() &amp;lt;= 32"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000005_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. Name length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000005_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryNameLength: self.name-&amp;gt;size() &amp;lt;= 32"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000006_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. ShortName length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000006_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryShortNameLength: self.shortName-&amp;gt;size() &amp;lt;= 12"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000007_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. To End ISO Code length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000007_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryToEndIsoCodeLength: self.toEndIsoCode-&amp;gt;size() = 2"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000008_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. To End Name length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000008_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryToEndNameLength: self.toEndName-&amp;gt;size() &amp;lt;= 32"/>
								</ownedRule>
								<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000009_FCC6_4af8_984C_2845ACE54737" name="R.4.10.11. To End Name TSO length restriction">
									<constrainedElement xmi:idref="EAID_OR000000_FCC6_4af8_984C_2845ACE54737"/>
									<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_COE000009_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryToEndNameTsoLength: self.toEndNameTso-&amp;gt;size() &amp;lt;= 32"/>
								</ownedRule>
							</specification>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000001_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryEnergyIdentCodeEicLength: self.energyIdentCodeEic = null or self.energyIdentCodeEic-&amp;gt;size() = 16"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000002_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryFromEndIsoCodeLength: self.fromEndIsoCode-&amp;gt;size() = 2"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000003_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryFromEndNameLength: self.fromEndName-&amp;gt;size() &amp;lt;= 32"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000004_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryFromEndNameTsoLength: self.fromEndNameTso-&amp;gt;size() &amp;lt;= 32"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000005_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryNameLength: self.name-&amp;gt;size() &amp;lt;= 32"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000006_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryShortNameLength: self.shortName-&amp;gt;size() &amp;lt;= 12"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000007_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryToEndIsoCodeLength: self.toEndIsoCode-&amp;gt;size() = 2"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000008_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryToEndNameLength: self.toEndName-&amp;gt;size() &amp;lt;= 32"/>
						</ownedRule>
						<ownedRule xmi:type="uml:Constraint" xmi:id="EAID_OR000009_FCC6_4af8_984C_2845ACE54737">
							<constrainedElement xmi:idref="EAID_919623A3_FCC6_4af8_984C_2845ACE54737"/>
							<specification xmi:type="uml:OpaqueExpression" xmi:id="EAID_OE000000_FCC6_4af8_984C_2845ACE54737" body="inv topologyBoundaryToEndNameTsoLength: self.toEndNameTso-&amp;gt;size() &amp;lt;= 32"/>
						</ownedRule>
					</packagedElement>
				</packagedElement>
...
						<packagedElement xmi:type="uml:Class" xmi:id="EAID_6B555DBD_D6CC_4eef_BB08_C4FA090797CD" name="SvVoltage">
							<ownedAttribute xmi:type="uml:Property" xmi:id="EAID_4F54F252_5AFE_445c_B9AC_DB0D79CCD171" name="angle">
								<type xmi:idref="EAID_2C503787_F407_4afc_AB13_D0AFD33066C1"/>
								<lowerValue xmi:type="uml:LiteralInteger" xmi:id="EAID_LI001683_5AFE_445c_B9AC_DB0D79CCD171" value="1"/>
								<upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="EAID_LI001684_5AFE_445c_B9AC_DB0D79CCD171" value="1"/>
							</ownedAttribute>
							<ownedAttribute xmi:type="uml:Property" xmi:id="EAID_F2E1312B_88E9_4912_925F_A7827B19A2AF" name="v">
								<type xmi:idref="EAID_879A7B06_25F5_4f30_B20A_371CE9B9789D"/>
								<lowerValue xmi:type="uml:LiteralInteger" xmi:id="EAID_LI001685_88E9_4912_925F_A7827B19A2AF" value="1"/>
								<upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="EAID_LI001686_88E9_4912_925F_A7827B19A2AF" value="1"/>
							</ownedAttribute>
							<ownedAttribute xmi:type="uml:Property" xmi:id="EAID_src49D0C4_3243_4314_900C_1DF99F8F8CEA" name="TopologicalNode" association="EAID_4549D0C4_3243_4314_900C_1DF99F8F8CEA">
								<type xmi:idref="EAID_05B1DE58_5F2D_4e1a_946C_B60BDCB3147B"/>
								<lowerValue xmi:type="uml:LiteralInteger" xmi:id="EAID_LI001687__3243_4314_900C_1DF99F8F8CEA" value="1"/>
								<upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="EAID_LI001688__3243_4314_900C_1DF99F8F8CEA" value="1"/>
							</ownedAttribute>
						</packagedElement>
                                               
....
			<connector xmi:idref="EAID_D2E8CC69_6B0D_4976_B750_F8036485E819">
				<source xmi:idref="EAID_49AB33F4_22AA_4fbb_9155_B5DD68D3D61E">
					<model ea_localid="26133" type="Class" name="SvTapStep"/>
					<role visibility="Public"/>
					<type aggregation="none"/>
					<constraints/>
					<modifiers isOrdered="false" isNavigable="false"/>
					<style value="Owned=0;Navigable=Non-Navigable;"/>
					<documentation/>
					<xrefs/>
					<tags/>
				</source>
				<target xmi:idref="EAID_EDA41BC3_4A8F_46d0_851F_EFCAB8942211">
					<model ea_localid="13442" type="Class" name="SvTapStep"/>
					<role visibility="Public"/>
					<type aggregation="none"/>
					<constraints/>
					<modifiers isOrdered="false" isNavigable="false"/>
					<style value="Owned=0;Navigable=Navigable;"/>
					<documentation/>
					<xrefs/>
					<tags/>
				</target>
				<model ea_localid="30246"/>
				<properties ea_type="Dependency" stereotype="IsBasedOn" direction="Source -&gt; Destination"/>
				<documentation/>
				<appearance linemode="3" linecolor="-1" linewidth="0" seqno="0" headStyle="0" lineStyle="0"/>
				<labels mb=" &#xA;«IsBasedOn»"/>
				<extendedProperties conditional=" &#xA;«IsBasedOn»" virtualInheritance="0"/>
				<style/>
				<xrefs/>
				<tags/>
			</connector>
            ...

			<element xmi:idref="EAID_6B555DBD_D6CC_4eef_BB08_C4FA090797CD" xmi:type="uml:Class" name="SvVoltage" scope="public">
				<model package="EAPK_96787AD7_9F16_4238_BB08_F60DD281F0DB" tpos="6" ea_localid="26134" ea_eleType="element"/>
				<properties documentation="State variable for voltage." isSpecification="false" sType="Class" nType="0" scope="public" isRoot="false" isLeaf="false" isAbstract="false" isActive="false"/>
				<project author="andre" version="1.0" phase="1.0" created="2011-02-24 15:43:52" modified="2014-05-25 09:32:43" complexity="1" status="Proposed"/>
				<code gentype="Java"/>
				<style appearance="BackColor=-1;BorderColor=-1;BorderWidth=-1;FontColor=-1;VSwimLanes=1;HSwimLanes=1;BorderStyle=0;"/>
				<tags>
					<tag xmi:id="EAID_A84893B4_EBFC_4ff2_B98C_1AFEC26CE972" name="GUIDBasedOn" value="{22A26B24-0A8E-402a-895E-AFAE18292542}" modelElement="EAID_6B555DBD_D6CC_4eef_BB08_C4FA090797CD"/>
				</tags>
				<xrefs value="$XREFPROP=$XID={FDC1B076-F65E-4ff2-91DA-D40E881CDCF8}$XID;$NAM=CustomProperties$NAM;$TYP=element property$TYP;$VIS=Public$VIS;$PAR=0$PAR;$DES=@PROP=@NAME=isActive@ENDNAME;@TYPE=Boolean@ENDTYPE;@VALU=@ENDVALU;@PRMT=@ENDPRMT;@ENDPROP;$DES;$CLT={6B555DBD-D6CC-4eef-BB08-C4FA090797CD}$CLT;$SUP=&lt;none&gt;$SUP;$ENDXREF;"/>
				<extendedProperties tagged="0" package_name="StateVariables"/>
				<attributes>
					<attribute xmi:idref="EAID_4F54F252_5AFE_445c_B9AC_DB0D79CCD171" name="angle" scope="Public">
						<initial/>
						<documentation value="The voltage angle of the topological node complex voltage with respect to system reference.&#xA;"/>
						<model ea_localid="95069" ea_guid="{4F54F252-5AFE-445c-B9AC-DB0D79CCD171}"/>
						<properties type="AngleDegrees" derived="0" precision="0" collection="false" length="0" duplicates="0" changeability="changeable"/>
						<coords ordered="0" scale="0"/>
						<containment containment="Not Specified" position="0"/>
						<stereotype/>
						<bounds lower="1" upper="1"/>
						<options/>
						<style/>
						<styleex value="IsLiteral=0;volatile=0;"/>
						<tags>
							<tag xmi:id="EAID_EA997565_4D43_4b89_952E_775E0024577F" name="GUIDBasedOn" value="{1D320E89-265C-41ec-A654-A0FE668376BD}"/>
						</tags>
						<xrefs value="$XREFPROP=$XID={62BFA906-5EDF-4c53-8A56-FD005866F04E}$XID;$NAM=CustomProperties$NAM;$TYP=attribute property$TYP;$VIS=Public$VIS;$PAR=0$PAR;$DES=@PROP=@NAME=isID@ENDNAME;@TYPE=Boolean@ENDTYPE;@VALU=0@ENDVALU;@PRMT=@ENDPRMT;@ENDPROP;$DES;$CLT={4F54F252-5AFE-445c-B9AC-DB0D79CCD171}$CLT;$SUP=&lt;none&gt;$SUP;$ENDXREF;"/>
					</attribute>
					<attribute xmi:idref="EAID_F2E1312B_88E9_4912_925F_A7827B19A2AF" name="v" scope="Public">
						<initial/>
						<documentation value="The voltage magnitude of the topological node."/>
						<model ea_localid="95070" ea_guid="{F2E1312B-88E9-4912-925F-A7827B19A2AF}"/>
						<properties type="Voltage" derived="0" precision="0" collection="false" length="0" duplicates="0" changeability="changeable"/>
						<coords ordered="0" scale="0"/>
						<containment containment="Not Specified" position="1"/>
						<stereotype/>
						<bounds lower="1" upper="1"/>
						<options/>
						<style/>
						<styleex/>
						<tags>
							<tag xmi:id="EAID_1869FADA_E456_4653_996F_B7A06FA429E2" name="GUIDBasedOn" value="{B4D2EA92-2DE6-41bb-9362-77F68809B646}"/>
						</tags>
						<xrefs value="$XREFPROP=$XID={618FCD44-1B35-4473-BFC6-8E934FF9C42E}$XID;$NAM=CustomProperties$NAM;$TYP=attribute property$TYP;$VIS=Public$VIS;$PAR=0$PAR;$DES=@PROP=@NAME=isID@ENDNAME;@TYPE=Boolean@ENDTYPE;@VALU=0@ENDVALU;@PRMT=@ENDPRMT;@ENDPROP;$DES;$CLT={F2E1312B-88E9-4912-925F-A7827B19A2AF}$CLT;$SUP=&lt;none&gt;$SUP;$ENDXREF;"/>
					</attribute>
				</attributes>
				<links>
					<Dependency xmi:id="EAID_922E523E_23B8_4474_839C_66540E22A755" start="EAID_6B555DBD_D6CC_4eef_BB08_C4FA090797CD" end="EAID_22A26B24_0A8E_402a_895E_AFAE18292542"/>
					<Association xmi:id="EAID_4549D0C4_3243_4314_900C_1DF99F8F8CEA" start="EAID_05B1DE58_5F2D_4e1a_946C_B60BDCB3147B" end="EAID_6B555DBD_D6CC_4eef_BB08_C4FA090797CD"/>
				</links>
			</element>

SmallGridTestConfiguration_BC_EQ_v3.0.0.xml file chunks
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/2013/CIM-schema-cim16#" xmlns:entsoe="http://entsoe.eu/CIM/SchemaExtension/3/1#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <md:FullModel rdf:about="urn:uuid:2399cbd2-9a39-11e0-aa80-0800200c9a66_EU">
    <md:Model.scenarioTime>2030-01-02T09:00:00</md:Model.scenarioTime>
    <md:Model.created>2015-02-02T13:01:25.830</md:Model.created>
    <md:Model.description>CGMES Conformity Assessment: Small Grid Base Case Test Configuration. The model is owned by ENTSO-E and is provided by ENTSO-E "as it is". To the fullest extent permitted by law, ENTSO-E shall not be liable for any damages of any kind arising out of the use of the model (including any of its subsequent modifications). ENTSO-E neither warrants, nor represents that the use of the model will not infringe the rights of third parties. Any use of the model shall include a reference to ENTSO-E. ENTSO-E web site is the only official source of information related to the model.</md:Model.description>
    <md:Model.version>4</md:Model.version>
    <md:Model.profile>http://entsoe.eu/CIM/EquipmentCore/3/1</md:Model.profile>
    <md:Model.modelingAuthoritySet>http://GB/Planning/ENTSOE/2</md:Model.modelingAuthoritySet>
    <md:Model.DependentOn rdf:resource="urn:uuid:2399cbd0-9a39-11e0-aa80-0800200c9a66" />
  </md:FullModel>
  <cim:Terminal rdf:ID="_0471bd25-c766-11e1-8775-005056c00008">
    <cim:IdentifiedObject.name>31-32_0</cim:IdentifiedObject.name>
    <cim:ACDCTerminal.sequenceNumber>1</cim:ACDCTerminal.sequenceNumber>
    <cim:Terminal.phases rdf:resource="http://iec.ch/TC57/2013/CIM-schema-cim16#PhaseCode.ABC" />
    <cim:Terminal.ConductingEquipment rdf:resource="#_044cd006-c766-11e1-8775-005056c00008" />
  </cim:Terminal>


  SmallGridTestConfiguration_BC_SSH_v3.0.0.xml head:
  <?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/2013/CIM-schema-cim16#" xmlns:entsoe="http://entsoe.eu/CIM/SchemaExtension/3/1#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <md:FullModel rdf:about="urn:uuid:2399cbd7-9a39-11e0-aa80-0800200c9a66_EU">
    <md:Model.scenarioTime>2030-01-02T09:00:00</md:Model.scenarioTime>
    <md:Model.created>2014-10-22T09:01:25.830</md:Model.created>
    <md:Model.description>CGMES Conformity Assessment: Small Grid Base Case Test Configuration. The model is owned by ENTSO-E and is provided by ENTSO-E "as it is". To the fullest extent permitted by law, ENTSO-E shall not be liable for any damages of any kind arising out of the use of the model (including any of its subsequent modifications). ENTSO-E neither warrants, nor represents that the use of the model will not infringe the rights of third parties. Any use of the model shall include a reference to ENTSO-E. ENTSO-E web site is the only official source of information related to the model.</md:Model.description>
    <md:Model.version>4</md:Model.version>
	<md:Model.profile>http://entsoe.eu/CIM/SteadyStateHypothesis/1/1</md:Model.profile>
    <md:Model.modelingAuthoritySet>http://GB/Planning/ENTSOE/2</md:Model.modelingAuthoritySet>
    <md:Model.DependentOn rdf:resource="urn:uuid:2399cbd2-9a39-11e0-aa80-0800200c9a66_EU" />
  </md:FullModel>
  <cim:Terminal rdf:about="#_0471bd25-c766-11e1-8775-005056c00008">
    <cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected>
  </cim:Terminal>
  <cim:Terminal rdf:about="#_04682030-c766-11e1-8775-005056c00008">
    <cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected>
  </cim:Terminal>



"""