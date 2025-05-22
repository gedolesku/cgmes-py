from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.SubGeographicalRegion import SubGeographicalRegion     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCEquipmentContainer import DCEquipmentContainer

@dataclass
class DCLine(DCEquipmentContainer):
    """Overhead lines and/or cables connecting two or more HVDC substations.
    """
    Region_ref: Optional[SubGeographicalRegion] = None
    Region: str = None
     