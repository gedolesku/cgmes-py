from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.SubGeographicalRegion import SubGeographicalRegion     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCEquipmentContainer import DCEquipmentContainer

@dataclass
class DCLine(DCEquipmentContainer):
    """Overhead lines and/or cables connecting two or more HVDC substations.
    """
    SubGeographicalRegion_: Optional[SubGeographicalRegion] = None
     