from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramObjectGluePoint import DiagramObjectGluePoint     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramObject import DiagramObject     

@dataclass
class DiagramObjectPoint:
    """A point in a given space defined by 3 coordinates and associated to a diagram
    object.  The coordinates may be positive or negative as the origin does not
    have to be in the corner of a diagram.
    """
    # The sequence position of the point, used for defining the order of points for
    # diagram objects acting as a polyline or polygon with more than one point.
    sequenceNumber: int  = None
 
    # The X coordinate of this point.
    xPosition: Simple_Float  = None
 
    # The Y coordinate of this point.
    yPosition: Simple_Float  = None
 
    # The Z coordinate of this point.
    zPosition: Simple_Float  = None
 
    # A diagram object glue point is associated with 2 or more object points that are
    # considered to be 'glued' together.
    DiagramObjectGluePoint_ref: Optional[DiagramObjectGluePoint] = None
    DiagramObjectGluePoint: str = None
 
    # The diagram object with which the points are associated.
    DiagramObject_ref: Optional[DiagramObject] = None
    DiagramObject: str = None
     