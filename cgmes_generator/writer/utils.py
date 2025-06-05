"""Writer utility functions."""

from __future__ import annotations

import re
from typing import List, Tuple

from ..meta import ClassMeta


def _rel_mod(src: Tuple[str, ...], dst: Tuple[str, ...], name: str) -> str:
    """Return relative module path for importing *name* located in *dst* when inside *src*."""
    common = 0
    for a, b in zip(src, dst):
        if a != b:
            break
        common += 1
    up = len(src) - common
    dots = '.' * (up + 1)
    rest = '.'.join(dst[common:] + (name,))
    return f"{dots}{rest}"


def py_imports(meta: ClassMeta) -> Tuple[List[str], str | None]:
    imps = {"from __future__ import annotations"}
    if meta.is_abstract:
        imps.add("from typing import Protocol, runtime_checkable")
    else:
        imps.add("from dataclasses import dataclass, field")
    needs_typing = any(
        a.type_.startswith("Optional[") or a.type_.startswith("list[")
        for a in meta.attrs.values()
    )
    if needs_typing:
        imps.add("from typing import Optional, List")
    imps.add(f"from {'.' * (len(meta.pkg_parts) + 1)}base import CIMObject")
    parent_alias = meta.parent
    if meta.parent and meta.parent_pkg:
        path = _rel_mod(meta.pkg_parts, meta.parent_pkg, meta.parent)
        alias = meta.parent
        if meta.parent == meta.name and meta.parent_pkg != meta.pkg_parts:
            alias = f"{meta.parent}_base"
        imps.add(
            f"from {path} import {meta.parent}" + (f" as {alias}" if alias != meta.parent else "")
        )
        parent_alias = alias
    for a in meta.attrs.values():
        base = a.type_
        m = re.fullmatch(r"Optional\[(.*)\]", base)
        if m:
            base = m.group(1)
        m = re.fullmatch(r"list\[(.*)\]", base)
        if m:
            base = m.group(1)
        if a.ref_pkg:
            if base != meta.name or a.ref_pkg != meta.pkg_parts:
                path = _rel_mod(meta.pkg_parts, a.ref_pkg, base)
                imps.add(f"from {path} import {base}")
    return sorted(imps, key=lambda s: (0 if s.startswith("from __future__") else 1, s)), parent_alias
