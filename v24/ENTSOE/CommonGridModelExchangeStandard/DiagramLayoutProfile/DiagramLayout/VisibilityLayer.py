from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramObject import DiagramObject     

@dataclass
class VisibilityLayer(IdentifiedObject):
    """Layers are typically used for grouping diagram objects according to themes and
    scales. Themes are used to display or hide certain information (e.g., lakes,
    borders), while scales are used for hiding or displaying information depending
    on the current zoom level (hide text when it is too small to be read, or when
    it exceeds the screen size). This is also called de-cluttering.
    
      CIM based graphics exchange will support an m:n relationship between diagram
    objects and layers. It will be the task of the importing system to convert an m:
    n case into an appropriate 1:n representation if the importing system does not
    support m:n.
    """
    # The drawing order for this layer.  The higher the number, the later the layer
    # and the objects within it are rendered.
    drawingOrder_: int  = None
 
    # A visibility layer can contain one or more diagram objects.
    DiagramObject_: List[DiagramObject]  = field(default_factory=list)
     