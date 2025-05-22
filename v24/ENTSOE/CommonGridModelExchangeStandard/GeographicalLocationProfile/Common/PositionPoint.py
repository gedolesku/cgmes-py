from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.GeographicalLocationProfile.Common.Location import Location     

@dataclass
class PositionPoint:
    """Set of spatial coordinates that determine a point, defined in the coordinate
    system specified in 'Location.CoordinateSystem'. Use a single position point
    instance to desribe a point-oriented location. Use a sequence of position
    points to describe a line-oriented object (physical location of non-point
    oriented objects like cables or lines), or area of an object (like a substation
    or a geographical zone - in this case, have first and last position point with
    the same values).
    """
    # Zero-relative sequence number of this point within a series of points.
    sequenceNumber: int  = None
 
    # X axis position.
    xPosition: str  = None
 
    # Y axis position.
    yPosition: str  = None
 
    # (if applicable) Z axis position.
    zPosition: str  = None
 
    # Location described by this position point.
    Location_ref: Optional[Location] = None
    Location: str = None
     