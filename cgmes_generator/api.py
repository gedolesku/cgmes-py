"""Public API for dataclass generation."""

from __future__ import annotations

from pathlib import Path

from .parser import load_xmi, parse_xmi
from .writer import BASE_SRC, write_classes, write_enums


def generate_dataclasses(xmi: str | Path, output_dir: str | Path) -> int:
    """Parse *xmi* and write dataclasses into *output_dir*."""
    tree = load_xmi(Path(xmi))
    classes, enums, _ = parse_xmi(tree)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "__init__.py").touch(exist_ok=True)
    (out_dir / "base.py").write_text(BASE_SRC, encoding="utf-8")
    n_enum = write_enums(enums, out_dir)
    n_cls = write_classes(classes, enums, out_dir)
    print(f"✅ Generisano {n_enum} enumeracija i {n_cls} klasa.")
    return n_enum + n_cls
