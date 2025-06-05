from __future__ import annotations
from ..Core.SubGeographicalRegion import SubGeographicalRegion
from .DCEquipmentContainer import DCEquipmentContainer
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCLine(DCEquipmentContainer):
    Region_id: str | None = field(default=None, metadata={"xpath": "cim:DCLine.Region/@rdf:resource", "pattern": r"^#.+$"})
    Region_ref: SubGeographicalRegion | None = None
