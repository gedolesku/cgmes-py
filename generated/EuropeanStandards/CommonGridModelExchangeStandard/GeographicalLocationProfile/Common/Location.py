from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.PowerSystemResource import PowerSystemResource
from .CoordinateSystem import CoordinateSystem
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Location(IdentifiedObject):
    PowerSystemResources_id: str | None = field(default=None, metadata={"xpath": "cim:Location.PowerSystemResources/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    PowerSystemResources_ref: PowerSystemResource = None
    CoordinateSystem_id: str | None = field(default=None, metadata={"xpath": "cim:Location.CoordinateSystem/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    CoordinateSystem_ref: CoordinateSystem = None
