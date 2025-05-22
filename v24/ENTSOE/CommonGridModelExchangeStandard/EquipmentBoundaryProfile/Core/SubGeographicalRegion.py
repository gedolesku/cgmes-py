from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Wires.Line import Line     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.GeographicalRegion import GeographicalRegion     

@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """A subset of a geographical region of a power system network model.
    """
    # The sub-geographical region of the line.
    Line_: List[Line]  = field(default_factory=list)
 
    # The geographical region to which this sub-geographical region is within.
    GeographicalRegion_: Optional[GeographicalRegion] = None
     