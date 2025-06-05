from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable

from .parser import load_xmi, parse_xmi
from .meta import ClassMeta, Attribute

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
        xp_base = f"cim:{meta.name}.{attr.name}"
        if attr.is_ref:
            lower = attr.multiplicity.split("..", 1)[0]
            required = lower == "1"
            id_type = "str" if required else "Optional[str]"
            meta_parts = [f'"xpath": "{xp_base}/@rdf:resource"']
            if required:
                meta_parts.append('"required": True')
            meta_parts.append('"pattern": "^#.+$"')
            meta_str = "{" + ", ".join(meta_parts) + "}"
            id_kwargs = f"metadata={meta_str}"
            if not required:
                id_kwargs = f"default=None, {id_kwargs}"
            lines.append(f"    {attr.name}_id: {id_type} = field({id_kwargs})")
            ref_default = " = None" if attr.type_.startswith("Optional[") else ""
            lines.append(f"    {attr.name}_ref: {attr.type_}{ref_default}")
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
        src = _gen_class(meta)
        (out_dir / f"{name}.py").write_text(src, encoding="utf-8")
