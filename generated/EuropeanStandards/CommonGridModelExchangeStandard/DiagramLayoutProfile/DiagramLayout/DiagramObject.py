from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Simple_Float import Simple_Float
from ..Core.IdentifiedObject import IdentifiedObject
from .Diagram import Diagram
from .DiagramObjectStyle import DiagramObjectStyle
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DiagramObject(IdentifiedObject):
    Diagram_id: str | None = field(default=None, metadata={"xpath": "cim:DiagramObject.Diagram/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Diagram_ref: Diagram = None
    drawingOrder: Optional[Integer] = field(default=None, metadata={'xpath': 'cim:DiagramObject.drawingOrder'})
    isPolygon: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:DiagramObject.isPolygon'})
    offsetX: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:DiagramObject.offsetX'})
    offsetY: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:DiagramObject.offsetY'})
    rotation: Optional[AngleDegrees] = field(default=None, metadata={'xpath': 'cim:DiagramObject.rotation'})
    DiagramObjectStyle_id: str | None = field(default=None, metadata={"xpath": "cim:DiagramObject.DiagramObjectStyle/@rdf:resource", "pattern": r"^#.+$"})
    DiagramObjectStyle_ref: DiagramObjectStyle | None = None
    IdentifiedObject_id: str | None = field(default=None, metadata={"xpath": "cim:DiagramObject.IdentifiedObject/@rdf:resource", "pattern": r"^#.+$"})
    IdentifiedObject_ref: IdentifiedObject | None = None
