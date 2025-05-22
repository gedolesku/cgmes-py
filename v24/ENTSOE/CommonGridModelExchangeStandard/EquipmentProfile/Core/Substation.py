from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.VoltageLevel import VoltageLevel     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.EquipmentContainer import EquipmentContainer
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.SubGeographicalRegion import SubGeographicalRegion     

@dataclass
class Substation(EquipmentContainer):
    """A collection of equipment for purposes other than generation or utilization,
    through which electric energy in bulk is passed for the purposes of switching
    or modifying its characteristics.
    """
    # The voltage levels within this substation.
    VoltageLevel_: List[VoltageLevel]  = field(default_factory=list)
 
    # The SubGeographicalRegion containing the substation.
    SubGeographicalRegion_: Optional[SubGeographicalRegion] = None
     