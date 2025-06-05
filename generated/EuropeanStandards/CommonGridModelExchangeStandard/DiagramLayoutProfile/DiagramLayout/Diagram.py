from __future__ import annotations
from ...DomainProfile.OrientationKind import OrientationKind
from ...DomainProfile.Simple_Float import Simple_Float
from ..Core.IdentifiedObject import IdentifiedObject
from .DiagramStyle import DiagramStyle
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Diagram(IdentifiedObject):
    orientation: OrientationKind = field(metadata={'xpath': 'cim:Diagram.orientation'})
    x1InitialView: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:Diagram.x1InitialView'})
    x2InitialView: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:Diagram.x2InitialView'})
    y1InitialView: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:Diagram.y1InitialView'})
    y2InitialView: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:Diagram.y2InitialView'})
    DiagramStyle_id: str | None = field(default=None, metadata={"xpath": "cim:Diagram.DiagramStyle/@rdf:resource", "pattern": r"^#.+$"})
    DiagramStyle_ref: DiagramStyle | None = None
