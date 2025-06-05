from __future__ import annotations
from .EquipmentContainer import EquipmentContainer
from .SubGeographicalRegion import SubGeographicalRegion
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Substation(EquipmentContainer):
    Region_id: str | None = field(default=None, metadata={"xpath": "cim:Substation.Region/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Region_ref: SubGeographicalRegion = None
