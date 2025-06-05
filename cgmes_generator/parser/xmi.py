"""Main XMI parsing entry point."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

from lxml import etree
from rdflib import Namespace

from ..meta import Attribute, ClassMeta, EnumMeta, LinkData
from .multiplicity import mult_from_elem, ptype

DEBUG = False  # set True for verbose output

# Namespaces used in the XMI
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


def collect_links(
    root: etree._Element,
    class_by_id: Dict[str, List[ClassMeta]],
) -> List[LinkData]:
    """Collect :class:`LinkData` objects and update ``ClassMeta.links``.

    The function also sets ``parent`` relationships based on ``Generalization``
    and ``Dependency`` links.
    """

    links: List[LinkData] = []

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

    for lnk in links:
        if lnk.kind == 'Generalization' and lnk.start in class_by_id and lnk.end in class_by_id:
            parent = class_by_id[lnk.end][0]
            for child in class_by_id[lnk.start]:
                if child.parent is None:
                    child.parent = parent.name
                    child.parent_pkg = parent.pkg_parts
        if lnk.kind == 'Dependency' and lnk.start in class_by_id and lnk.end in class_by_id:
            parent = class_by_id[lnk.end][0]
            for child in class_by_id[lnk.start]:
                if child.parent is None and child.pkg_parts != parent.pkg_parts:
                    child.parent = parent.name
                    child.parent_pkg = parent.pkg_parts

    return links


def parse_xmi(tree: etree._ElementTree) -> Tuple[
    Dict[Tuple[str, ...], ClassMeta],
    Dict[Tuple[str, ...], EnumMeta],
    List[LinkData],
]:
    """Parse the XMI tree into metadata structures."""
    root = tree.getroot()
    by_id = {e.get(f"{{{XMI_NS}}}id"): e for e in root.iter() if e.get(f"{{{XMI_NS}}}id")}

    prim_elems = root.xpath(".//packagedElement[@xmi:type='uml:PrimitiveType']", namespaces=NSMAP)
    primitive_ids = {e.get(f"{{{XMI_NS}}}id"): PRIMITIVE_MAP.get(e.get("name")) for e in prim_elems}

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
    links: List[LinkData] = []

    for en in root.xpath(".//packagedElement[@xmi:type='uml:Enumeration']", namespaces=NSMAP):
        ename = en.get("name")
        if not ename:
            continue
        pkg = id_to_pkg.get(en.get(f"{{{XMI_NS}}}id"), ())
        e_doc = en.find("ownedComment/Body")
        key = pkg + (ename,)
        meta = EnumMeta(
            ename,
            [l.get("name") for l in en.xpath("./ownedLiteral")],
            pkg,
            e_doc.text if e_doc is not None else None,
        )
        enums[key] = meta
        enum_by_id[en.get(f"{{{XMI_NS}}}id")] = meta

    def walk(elem, pkg_path: List[str]):
        for child in elem.xpath("./packagedElement"):
            kind = child.get(f"{{{XMI_NS}}}type")
            if kind == "uml:Package":
                walk(child, pkg_path + [child.get("name")])
                continue
            if kind != "uml:Class":
                continue
            cname = child.get("name")
            if not cname:
                continue
            if DEBUG:
                print("🔍 Klasa", cname)
            c_doc = child.find("ownedComment/Body")
            meta = ClassMeta(
                cname,
                {},
                None,
                tuple(pkg_path),
                c_doc.text if c_doc is not None else None,
                None,
                child.get(f"{{{XMI_NS}}}id"),
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

            for prop in child.xpath("./ownedAttribute"):
                a_name = prop.get("name")
                type_ref = prop.get("type")
                if type_ref is None:
                    t_elem = prop.find("type")
                    if t_elem is not None:
                        type_ref = t_elem.get(f"{{{XMI_NS}}}idref")
                lower, upper = mult_from_elem(prop)
                if type_ref in primitive_ids:
                    base_type = primitive_ids[type_ref]
                    ref_pkg = None
                elif type_ref in class_by_id:
                    base_type = class_by_id[type_ref][0].name
                    ref_pkg = class_by_id[type_ref][0].pkg_parts
                elif type_ref in enum_by_id:
                    base_type = enum_by_id[type_ref].name
                    ref_pkg = enum_by_id[type_ref].pkg_parts
                elif type_ref in by_id:
                    elem = by_id[type_ref]
                    kind = elem.get(f"{{{XMI_NS}}}type")
                    if kind in ("uml:Class", "uml:Enumeration"):
                        base_type = elem.get("name", "str")
                        ref_pkg = id_to_pkg.get(type_ref)
                    else:
                        base_type = "str"
                        ref_pkg = None
                else:
                    base_type = "str"
                    ref_pkg = None
                is_ref = bool(prop.get("association"))
                target.attrs[a_name] = Attribute(
                    a_name,
                    f"cim:{cname}.{a_name}",
                    ptype(base_type, lower, upper),
                    f"{lower}..{upper}" if lower != upper else lower,
                    is_ref,
                    ref_pkg,
                    prop.get(f"{{{XMI_NS}}}id"),
                )

            gen = child.find("generalization")
            if gen is not None and (gid := gen.get("general")):
                if target.parent is None:
                    if gid in class_by_id:
                        target.parent = class_by_id[gid][0].name
                        target.parent_pkg = class_by_id[gid][0].pkg_parts
                    else:
                        target.parent = by_id.get(gid).get("name") if gid in by_id else None
                        target.parent_pkg = id_to_pkg.get(gid)

    for model in root.xpath(".//uml:Model", namespaces=NSMAP):
        walk(model, [])

    links = collect_links(root, class_by_id)

    for assoc in root.xpath(".//packagedElement[@xmi:type='uml:Association']", namespaces=NSMAP):
        ends = assoc.xpath("./ownedEnd | ./ownedAttribute")
        if len(ends) < 2:
            continue
        for end in ends:
            owner_id = end.get("type")
            if not owner_id:
                continue
            for other in ends:
                if other is end:
                    continue
                target_id = other.get("type")
                if not target_id:
                    continue
                if owner_id in class_by_id and target_id in class_by_id:
                    target_meta = class_by_id[target_id][0]
                    lower, upper = mult_from_elem(end)
                    for owner_meta in class_by_id[owner_id]:
                        owner_meta.attrs.setdefault(
                            end.get("name") or target_meta.name,
                            Attribute(
                                end.get("name") or target_meta.name,
                                f"cim:{owner_meta.name}.{end.get('name') or target_meta.name}",
                                ptype(target_meta.name, lower, upper),
                                f"{lower}..{upper}" if lower != upper else lower,
                                True,
                                target_meta.pkg_parts,
                                end.get(f"{{{XMI_NS}}}id"),
                            ),
                        )

    for metas in class_by_id.values():
        if len(metas) < 2:
            continue
        combined_attrs: Dict[str, Attribute] = {}
        parent_name = None
        parent_pkg = None
        doc = None
        for m in metas:
            combined_attrs.update(m.attrs)
            if m.parent and not parent_name:
                parent_name = m.parent
                parent_pkg = m.parent_pkg
            if m.doc and not doc:
                doc = m.doc
        for m in metas:
            for a_name, attr in combined_attrs.items():
                m.attrs.setdefault(a_name, attr)
            if parent_name and not m.parent:
                m.parent = parent_name
                m.parent_pkg = parent_pkg

    for meta in classes.values():
        if (
            'TopologyProfile' in '.'.join(meta.pkg_parts)
            and meta.name
        ):
            sv_key = (
                'EuropeanStandards',
                'CommonGridModelExchangeStandard',
                'StateVariablesProfile',
            ) + meta.pkg_parts[-1:] + (meta.name,)
            sv_meta = classes.get(sv_key)
            if sv_meta and sv_meta.name == meta.name:
                meta.parent = sv_meta.name
                meta.parent_pkg = sv_meta.pkg_parts

    print(
        "✅ klase:", len(classes), "– prim:", len(primitive_ids), "– enum:", len(enums)
    )
    return classes, enums, links
