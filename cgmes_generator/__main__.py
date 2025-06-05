from __future__ import annotations
import argparse
from .simple_gen import rebuild


def main() -> None:
    ap = argparse.ArgumentParser(description="CGMES code generator")
    ap.add_argument("--rebuild", action="store_true", help="generate built-in models")
    args = ap.parse_args()
    if args.rebuild:
        rebuild()


if __name__ == "__main__":
    main()
