from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.VisibilityLayer import VisibilityLayer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramObjectStyle import DiagramObjectStyle     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.Diagram import Diagram     

@dataclass
class DiagramObject(IdentifiedObject):
    """An object that defines one or more points in a given space. This object can be
    associated with anything that specializes IdentifiedObject. For single line
    diagrams such objects typically include such items as analog values, breakers,
    disconnectors, power transformers, and transmission lines.
    """
    # The drawing order of this element. The higher the number, the later the element
    # is drawn in sequence. This is used to ensure that elements that overlap are
    # rendered in the correct order.
    drawingOrder_: int  = None
 
    # Defines whether or not the diagram objects points define the boundaries of a
    # polygon or the routing of a polyline. If this value is true then a receiving
    # application should consider the first and last points to be connected.
    isPolygon_: bool  = None
 
    # The offset in the X direction. This is used for defining the offset from centre
    # for rendering an icon (the default is that a single point specifies the centre
    # of the icon).
    # 
    # The offset is in per-unit with 0 indicating there is no offset from the
    # horizontal centre of the icon.  -0.5 indicates it is offset by 50% to the left
    # and 0.5 indicates an offset of 50% to the right.
    offsetX_: Simple_Float  = None
 
    # The offset in the Y direction. This is used for defining the offset from centre
    # for rendering an icon (the default is that a single point specifies the centre
    # of the icon).
    # 
    # The offset is in per-unit with 0 indicating there is no offset from the
    # vertical centre of the icon.  The offset direction is dependent on the
    # orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50%
    # on the vertical axis.
    offsetY_: Simple_Float  = None
 
    # Sets the angle of rotation of the diagram object.  Zero degrees is pointing to
    # the top of the diagram.  Rotation is clockwise.
    rotation_: AngleDegrees  = None
 
    # The diagram objects that are associated with the domain object.
    IdentifiedObject_: Optional[IdentifiedObject] = None
 
    # A diagram object can be part of multiple visibility layers.
    VisibilityLayer_: List[VisibilityLayer]  = field(default_factory=list)
 
    # A diagram object has a style associated that provides a reference for the style
    # used in the originating system.
    DiagramObjectStyle_: Optional[DiagramObjectStyle] = None
 
    # A diagram object is part of a diagram.
    Diagram_: Optional[Diagram] = None
     