from __future__ import annotations
from pathlib import Path

TEMPLATES = {
    "IdentifiedObject": (Path(__file__).parent / "templates" / "IdentifiedObject.py.j2").read_text(encoding="utf-8"),
    "TopologicalNode": (Path(__file__).parent / "templates" / "TopologicalNode.py.j2").read_text(encoding="utf-8"),
}

def rebuild(out_dir: Path = Path("generated/topology")) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "__init__.py").touch()
    (out_dir / "IdentifiedObject.py").write_text(TEMPLATES["IdentifiedObject"], encoding="utf-8")
    (out_dir / "TopologicalNode.py").write_text(TEMPLATES["TopologicalNode"], encoding="utf-8")
