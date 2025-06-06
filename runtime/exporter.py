from __future__ import annotations

"""Helpers to serialize entire CGMES datasets.

The :func:`export_dataset` utility groups objects by profile name and writes
one XML file per profile.  It complements :func:`parse_dataset` for simple
round trips.
"""

from pathlib import Path
from typing import Mapping, Sequence, Type

from dataclasses import is_dataclass
from lxml import etree

from .base import to_element


def export_dataset(
    objects: Mapping[Type, Sequence[object]],
    out_dir: str | Path,
    *,
    namespace: str = "http://iec.ch/TC57/2013/CIM-schema-cim16#",
    pretty: bool = True,
) -> None:
    """Write one XML file per CGMES profile contained in *objects*.

    Parameters
    ----------
    objects:
        Mapping returned by :func:`parse_dataset` with classes as keys.
    out_dir:
        Target directory for the profile XML files.
    namespace:
        CIM namespace to use for the ``cim`` prefix in the output files.
    pretty:
        If ``True`` the XML is pretty printed with indentation.
    """

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Group objects by profile name taken from the module path
    grouped: dict[str, list[object]] = {}
    for cls, seq in objects.items():
        profile = cls.__module__.split(".")[-2]
        grouped.setdefault(profile, []).extend(seq)

    for profile, seq in grouped.items():
        root = etree.Element(
            "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF",
            nsmap={
                "cim": namespace,
                "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            },
        )
        for obj in seq:
            assert is_dataclass(obj), obj
            root.append(to_element(obj))

        path = out_dir / f"{profile}.xml"
        etree.ElementTree(root).write(
            path,
            encoding="utf-8",
            xml_declaration=True,
            pretty_print=pretty,
        )
