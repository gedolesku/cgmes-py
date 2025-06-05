"""XMI loading helpers."""

from __future__ import annotations

import zipfile
from pathlib import Path

from lxml import etree


def load_xmi(src: Path) -> etree._ElementTree:
    """Load an XMI file from *src* or from within a zip archive."""
    if not src.exists():
        raise FileNotFoundError(src)
    if src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src) as zf:
            name = next((n for n in zf.namelist() if n.lower().endswith((".xmi", ".xml"))), None)
            if not name:
                raise RuntimeError("ZIP ne sadrži .xmi/.xml")
            return etree.ElementTree(etree.fromstring(zf.read(name)))
    return etree.parse(str(src))
