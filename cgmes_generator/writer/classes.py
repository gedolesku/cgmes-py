"""Dataclass module generation."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

from ..meta import Attribute, ClassMeta, EnumMeta
from .utils import py_imports


def write_classes(
    classes: Dict[Tuple[str, ...], ClassMeta],
    enums: Dict[Tuple[str, ...], EnumMeta],
    out_dir: Path,
) -> int:
    """Write dataclass modules for all CGMES classes into *out_dir*."""
    cnt = 0
    for meta in classes.values():
        if not meta.name.isidentifier():
            continue
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)
        partial = out_dir
        for part in meta.pkg_parts:
            partial /= part
            (partial / "__init__.py").touch(exist_ok=True)

        imports, parent_alias = py_imports(meta)
        lines = imports
        parent = parent_alias
        if meta.is_abstract and not (
            meta.name == "TopologicalNode"
            and "StateVariablesProfile" in ".".join(meta.pkg_parts)
        ):
            parent_meta = None
            if meta.parent and meta.parent_pkg:
                parent_meta = classes.get(meta.parent_pkg + (meta.parent,))
            if parent_meta and parent_meta.is_abstract and parent_alias:
                bases = f"{parent_alias}, Protocol"
            else:
                bases = "Protocol"
            lines += ["", "@runtime_checkable"]
            lines.append(f"class {meta.name}({bases}):")
            parent = None
        else:
            lines += ["", "@dataclass(init=False)"]
            bases = []
            if parent_alias:
                bases.append(parent_alias)
            if meta.name == "TopologicalNode" and "TopologyProfile" in ".".join(
                meta.pkg_parts
            ):
                bases.append("IdentifiedObject")
            if bases:
                lines.append(f"class {meta.name}({', '.join(bases)}):")
            else:
                lines.append(f"class {meta.name}:")
        if meta.doc:
            lines.append(f'    """{meta.doc}"""')
        ordered_attrs = sorted(
            meta.attrs.values(),
            key=lambda a: (
                0
                if not (a.type_.startswith("Optional[") or a.type_.startswith("list["))
                else 1
            ),
        )
        if meta.name == "TopologicalNode":
            ordered_attrs.insert(
                0,
                Attribute(
                    "name", "cim:IdentifiedObject.name", "Optional[str]", "0..1", False
                ),
            )
            ordered_attrs.insert(
                0,
                Attribute("mRID", "@rdf:ID", "str", "1", False),
            )
        for a in ordered_attrs:
            if meta.is_abstract and not (
                meta.name == "TopologicalNode"
                and "StateVariablesProfile" in ".".join(meta.pkg_parts)
            ):
                if a.is_ref:
                    lines.append(
                        f"    {a.name}_ref: {a.type_}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
                    )
                    if not a.type_.startswith("list["):
                        lines.append(f"    {a.name}_id: str")
                else:
                    lines.append(
                        f"    {a.name}: {a.type_}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
                    )
            else:
                xp = a.cim_path
                if a.name == "mRID":
                    xp = "@rdf:ID"
                if a.is_ref:
                    xp += "/@rdf:resource"
                meta_parts = [f'"xpath": "{xp}"']
                if a.multiplicity in ("1", "1..1"):
                    meta_parts.append('"required": True')
                if a.is_ref:
                    meta_parts.append('"pattern": r"^#.+$"')
                meta_str = ", ".join(meta_parts)
                if a.is_ref:
                    lines.append(
                        f"    {a.name}_ref: {a.type_}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
                    )
                    if not a.type_.startswith("list["):
                        lines.append(
                            f"    {a.name}_id: str | None = field(default=None, metadata={{ {meta_str} }})"
                        )
                else:
                    if a.type_.startswith("list["):
                        default_expr = (
                            f"field(default_factory=list, metadata={{ {meta_str} }})"
                        )
                    else:
                        default_expr = f"field(default=None, metadata={{ {meta_str} }})"
                    lines.append(f"    {a.name}: {a.type_} = {default_expr}")
        if not meta.attrs:
            lines.append("    pass")
        (pkg_dir / f"{meta.name}.py").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )
        cnt += 1
    return cnt
