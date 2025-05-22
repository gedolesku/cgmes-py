from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.GeographicalLocationProfile.Core.PowerSystemResource import PowerSystemResource     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.GeographicalLocationProfile.Common.PositionPoint import PositionPoint     
from ENTSOE.CommonGridModelExchangeStandard.GeographicalLocationProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.GeographicalLocationProfile.Common.CoordinateSystem import CoordinateSystem     

@dataclass
class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has been, is,
    and/or will be at a given moment in time. It can be defined with one or more
    postition points (coordinates) in a given coordinate system.
    """
    # All power system resources at this location.
    PowerSystemResource_: Optional[PowerSystemResource] = None
 
    # Sequence of position points describing this location, expressed in coordinate
    # system 'Location.CoordinateSystem'.
    PositionPoint_: List[PositionPoint]  = field(default_factory=list)
 
    # Coordinate system used to describe position points of this location.
    CoordinateSystem_: Optional[CoordinateSystem] = None
     