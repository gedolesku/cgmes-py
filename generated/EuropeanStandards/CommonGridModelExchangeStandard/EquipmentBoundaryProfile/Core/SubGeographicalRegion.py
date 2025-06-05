from __future__ import annotations
from .GeographicalRegion import GeographicalRegion
from .IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SubGeographicalRegion(IdentifiedObject):
    Region_id: str | None = field(default=None, metadata={"xpath": "cim:SubGeographicalRegion.Region/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Region_ref: GeographicalRegion = None
