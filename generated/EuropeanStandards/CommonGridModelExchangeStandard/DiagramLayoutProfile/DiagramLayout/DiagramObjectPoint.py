from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Simple_Float import Simple_Float
from .DiagramObject import DiagramObject
from .DiagramObjectGluePoint import DiagramObjectGluePoint
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DiagramObjectPoint:
    xPosition: Simple_Float = field(metadata={'xpath': 'cim:DiagramObjectPoint.xPosition'})
    yPosition: Simple_Float = field(metadata={'xpath': 'cim:DiagramObjectPoint.yPosition'})
    DiagramObject_id: str | None = field(default=None, metadata={"xpath": "cim:DiagramObjectPoint.DiagramObject/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    DiagramObject_ref: DiagramObject = None
    sequenceNumber: Optional[Integer] = field(default=None, metadata={'xpath': 'cim:DiagramObjectPoint.sequenceNumber'})
    zPosition: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:DiagramObjectPoint.zPosition'})
    DiagramObjectGluePoint_id: str | None = field(default=None, metadata={"xpath": "cim:DiagramObjectPoint.DiagramObjectGluePoint/@rdf:resource", "pattern": r"^#.+$"})
    DiagramObjectGluePoint_ref: DiagramObjectGluePoint | None = None
