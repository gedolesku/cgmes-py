from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.OrientationKind import OrientationKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramStyle import DiagramStyle     

@dataclass
class Diagram(IdentifiedObject):
    """The diagram being exchanged.  The coordinate system is a standard Cartesian
    coordinate system and the orientation attribute defines the orientation.
    """
    # Coordinate system orientation of the diagram.
    orientation_: OrientationKind  = None
 
    # X coordinate of the first corner of the initial view.
    x1InitialView_: Simple_Float  = None
 
    # X coordinate of the second corner of the initial view.
    x2InitialView_: Simple_Float  = None
 
    # Y coordinate of the first corner of the initial view.
    y1InitialView_: Simple_Float  = None
 
    # Y coordinate of the second corner of the initial view.
    y2InitialView_: Simple_Float  = None
 
    # A Diagram may have a DiagramStyle.
    DiagramStyle_: Optional[DiagramStyle] = None
     