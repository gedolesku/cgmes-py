from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.EquipmentContainer import EquipmentContainer
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.SubGeographicalRegion import SubGeographicalRegion     

@dataclass
class Line(EquipmentContainer):
    """Contains equipment beyond a substation belonging to a power transmission line.
    """
    # The sub-geographical region of the line.
    SubGeographicalRegion_: Optional[SubGeographicalRegion] = None
     