from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable

from .parser import load_xmi, parse_xmi
from .meta import ClassMeta, Attribute
from .api import generate_dataclasses

TEMPLATES = {
    "IdentifiedObject": (
        Path(__file__).parent / "templates" / "IdentifiedObject.py.j2"
    ).read_text(encoding="utf-8"),
}

XMI_PATH = (
    Path(__file__).resolve().parents[1]
    / "cgmes-models"
    / "v24"
    / "ENTSOE_CGMES_v2.4.15_7Aug2014.xml"
)

TARGETS = {
    "TopologicalNode": "TopologyProfile",
    "ConnectivityNode": "TopologyProfile",
    "Terminal": "TopologyProfile",
    "SvVoltage": "StateVariablesProfile",
    "SvPowerFlow": "StateVariablesProfile",
    "SvInjection": "StateVariablesProfile",
    "SvTapStep": "StateVariablesProfile",
}


def _pick_class(
    classes: Dict[tuple[str, ...], ClassMeta], name: str, profile: str
) -> ClassMeta:
    for key, meta in classes.items():
        if meta.name == name and profile in key:
            return meta
    raise KeyError(name)


def _gen_class(meta: ClassMeta) -> str:
    imps = [
        "from __future__ import annotations",
        "from dataclasses import dataclass, field",
    ]
    needs_typing = any(
        a.type_.startswith("Optional[") or a.type_.startswith("list[")
        for a in meta.attrs.values()
    )
    if needs_typing:
        imps.append("from typing import Optional, List")
    imps.append("from .IdentifiedObject import IdentifiedObject")

    lines = ['"""Auto-generated — DO NOT EDIT BY HAND"""', ""]
    lines.extend(imps)
    lines.append("")
    lines.append(f"__all__ = ['{meta.name}']")
    lines.append("")
    lines.append("@dataclass(kw_only=True)")
    lines.append(f"class {meta.name}(IdentifiedObject):")
    lines.append('    """Auto-generated — DO NOT EDIT BY HAND"""')

    for attr in meta.attrs.values():
        xp_base = attr.cim_path
        if attr.is_ref:
            lower = attr.multiplicity.split("..", 1)[0]
            is_list = attr.type_.startswith("list[")
            id_hint = "list[str]" if is_list else "str"
            field_prefix = "default_factory=list" if is_list else "default=None"
            meta_parts = [f'"xpath": "{xp_base}/@rdf:resource"']
            if lower == "1":
                meta_parts.append('"required": True')
            meta_parts.append('"pattern": r"^#.+$"')
            meta_str = "{" + ", ".join(meta_parts) + "}"
            lines.append(
                f"    {attr.name}_id: {id_hint} | None = field({field_prefix}, metadata={meta_str})"
            )
            lines.append(
                f"    {attr.name}_ref: '{attr.type_.replace('Optional[', '').rstrip(']')}' | None = None"
            )
        else:
            field_kwargs = f"metadata={{'xpath': '{xp_base}'}}"
            if attr.type_.startswith("Optional["):
                field_kwargs = f"default=None, {field_kwargs}"
            elif attr.type_.startswith("list["):
                field_kwargs = f"default_factory=list, {field_kwargs}"
            lines.append(f"    {attr.name}: {attr.type_} = field({field_kwargs})")

    if not meta.attrs:
        lines.append("    pass")
    return "\n".join(lines) + "\n"


def rebuild(out_dir: Path = Path("generated/topology")) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "__init__.py").touch()
    (out_dir / "IdentifiedObject.py").write_text(
        TEMPLATES["IdentifiedObject"], encoding="utf-8"
    )

    classes, _enums, _links = parse_xmi(load_xmi(XMI_PATH))
    for name, profile in TARGETS.items():
        try:
            meta = _pick_class(classes, name, profile)
        except KeyError:
            continue
        if name in TEMPLATES:
            (out_dir / f"{name}.py").write_text(TEMPLATES[name], encoding="utf-8")
        else:
            src = _gen_class(meta)
            (out_dir / f"{name}.py").write_text(src, encoding="utf-8")

    eq_dir = Path("generated/equipment")
    _rebuild_equipment(eq_dir, classes)

    generate_dataclasses(XMI_PATH, Path("generated"))


def _rebuild_equipment(out: Path, classes: Dict[tuple[str, ...], ClassMeta]) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "__init__.py").touch()
    (out / "IdentifiedObject.py").write_text(
        TEMPLATES["IdentifiedObject"], encoding="utf-8"
    )
    targets = [
        m
        for m in classes.values()
        if m.stereotype == "Equipment" or "EquipmentProfile" in ".".join(m.pkg_parts)
    ]
    for meta in sorted(targets, key=lambda m: m.name):
        if meta.name in TEMPLATES:
            (out / f"{meta.name}.py").write_text(TEMPLATES[meta.name], encoding="utf-8")
        else:
            src = _gen_class(meta)
            (out / f"{meta.name}.py").write_text(src, encoding="utf-8")
