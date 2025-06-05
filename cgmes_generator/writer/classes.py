"""Dataclass module generation."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

from ..meta import ClassMeta, EnumMeta
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
        if meta.parent and meta.parent == meta.name:
            lines.append("# pylint: disable=function-redefined")
        parent = parent_alias
        if meta.is_abstract:
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
            lines += ["", "@dataclass(kw_only=True)"]
            bases = []
            if parent_alias:
                bases.append(parent_alias)
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
        for a in ordered_attrs:
            if meta.is_abstract:
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
                if a.is_ref:
                    lower = a.multiplicity.split("..", 1)[0]
                    is_list = a.type_.startswith("list[")
                    id_hint = "list[str]" if is_list else "str"
                    field_prefix = "default_factory=list" if is_list else "default=None"
                    meta_parts = [f'"xpath": "{a.cim_path}/@rdf:resource"']
                    if lower == "1":
                        meta_parts.append('"required": True')
                    meta_parts.append('"pattern": r"^#.+$"')
                    meta_str = "{" + ", ".join(meta_parts) + "}"
                    lines.append(
                        f"    {a.name}_id: {id_hint} | None = field({field_prefix}, metadata={meta_str})"
                    )
                    base = (
                        a.type_.replace("Optional[", "")
                        .replace("list[", "")
                        .rstrip("]")
                    )
                    ref_ann = base if lower == "1" else f"{base} | None"
                    lines.append(f"    {a.name}_ref: {ref_ann} = None")
                else:
                    field_kwargs = f"metadata={{'xpath': '{a.cim_path}'}}"
                    if a.type_.startswith("Optional["):
                        field_kwargs = f"default=None, {field_kwargs}"
                    elif a.type_.startswith("list["):
                        field_kwargs = f"default_factory=list, {field_kwargs}"
                    lines.append(f"    {a.name}: {a.type_} = field({field_kwargs})")
        if not meta.attrs:
            lines.append("    pass")
        (pkg_dir / f"{meta.name}.py").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )
        cnt += 1
    return cnt
