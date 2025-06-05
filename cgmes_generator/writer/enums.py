"""Enum generation."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

from ..meta import EnumMeta


def write_enums(enums: Dict[Tuple[str, ...], EnumMeta], out_dir: Path) -> int:
    """Write Enum classes for all UML enumerations."""
    cnt = 0
    for meta in enums.values():
        if not meta.name.isidentifier():
            continue
        pkg_dir = out_dir.joinpath(*meta.pkg_parts)
        pkg_dir.mkdir(parents=True, exist_ok=True)
        partial = out_dir
        for part in meta.pkg_parts:
            partial /= part
            (partial / "__init__.py").touch(exist_ok=True)

        lines = ["from enum import Enum", "", f"class {meta.name}(Enum):"]
        for lit in meta.literals:
            lines.append(f"    {lit} = '{lit}'")
        if not meta.literals:
            lines.append("    pass")
        (pkg_dir / f"{meta.name}.py").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )
        cnt += 1
    return cnt
