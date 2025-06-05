from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ..Core.IdentifiedObject import IdentifiedObject
from .DiagramObject import DiagramObject
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class VisibilityLayer(IdentifiedObject):
    drawingOrder: Optional[Integer] = field(default=None, metadata={'xpath': 'cim:VisibilityLayer.drawingOrder'})
    VisibleObjects_id: list[str] | None = field(default_factory=list, metadata={"xpath": "cim:VisibilityLayer.VisibleObjects/@rdf:resource", "pattern": r"^#.+$"})
    VisibleObjects_ref: DiagramObject | None = None
