"""Dataclass module generation."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

from ..meta import ClassMeta, EnumMeta
from .utils import py_imports


def write_classes(classes: Dict[Tuple[str, ...], ClassMeta], enums: Dict[Tuple[str, ...], EnumMeta], out_dir: Path) -> int:
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
        lines += ["", "@dataclass(init=False)"]
        parent = parent_alias or "CIMObject"
        lines.append(f"class {meta.name}({parent}):")
        if meta.doc:
            lines.append(f"    \"\"\"{meta.doc}\"\"\"")
        ordered_attrs = sorted(
            meta.attrs.values(),
            key=lambda a: 0 if not (a.type_.startswith("Optional[") or a.type_.startswith("list[")) else 1,
        )
        for a in ordered_attrs:
            default = ""
            if a.type_.startswith("Optional["):
                default = " = None"
            elif a.type_.startswith("list["):
                default = " = field(default_factory=list)"
            if a.is_ref:
                lines.append(
                    f"    {a.name}_ref: {a.type_}{default}  # metadata: cim='{a.cim_path}', mult='{a.multiplicity}'"
                )
                if not a.type_.startswith("list["):
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
