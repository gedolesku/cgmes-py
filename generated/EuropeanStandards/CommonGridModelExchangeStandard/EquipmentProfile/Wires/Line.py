from __future__ import annotations
from ..Core.EquipmentContainer import EquipmentContainer
from ..Core.SubGeographicalRegion import SubGeographicalRegion
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Line(EquipmentContainer):
    Region_id: str | None = field(default=None, metadata={"xpath": "cim:Line.Region/@rdf:resource", "pattern": r"^#.+$"})
    Region_ref: SubGeographicalRegion | None = None
