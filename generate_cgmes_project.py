#!/usr/bin/env python3
"""generate_dataclasses.py  –  CGMES 2.4 UML‑XMI → dataclasses
================================================================

This module is a thin wrapper around the :mod:`cgmes_generator` package
which contains the actual parsing and code generation logic.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from cgmes_generator import generate_dataclasses as _generate_dataclasses


def generate_dataclasses(xmi: str | Path, output_dir: str | Path) -> int:
    """Parse *xmi* and write dataclass modules into *output_dir*."""
    return _generate_dataclasses(xmi, output_dir)


def _cli() -> None:
    """Parse command line arguments and trigger dataclass generation."""
    ap = argparse.ArgumentParser(
        description=(
            "Generate CGMES dataclasses from XMI. Duplicate class definitions "
            "(same XMI id or package path) are merged so attributes may come "
            "from multiple packages."
        )
    )
    ap.add_argument("xmi")
    ap.add_argument("-o", "--output", required=True)
    args = ap.parse_args()
    generate_dataclasses(args.xmi, args.output)


if __name__ == "__main__":
    _cli()
