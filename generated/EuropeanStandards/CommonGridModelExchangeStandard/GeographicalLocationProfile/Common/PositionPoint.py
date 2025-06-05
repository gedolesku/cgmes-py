from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ...DomainProfile.String import String
from .Location import Location
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class PositionPoint:
    xPosition: String = field(metadata={'xpath': 'cim:PositionPoint.xPosition'})
    yPosition: String = field(metadata={'xpath': 'cim:PositionPoint.yPosition'})
    Location_id: str | None = field(default=None, metadata={"xpath": "cim:PositionPoint.Location/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Location_ref: Location = None
    sequenceNumber: Optional[Integer] = field(default=None, metadata={'xpath': 'cim:PositionPoint.sequenceNumber'})
    zPosition: Optional[String] = field(default=None, metadata={'xpath': 'cim:PositionPoint.zPosition'})
