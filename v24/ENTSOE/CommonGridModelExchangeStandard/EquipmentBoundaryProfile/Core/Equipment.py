from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.PowerSystemResource import PowerSystemResource
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.EquipmentContainer import EquipmentContainer     

@dataclass
class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanical.
    """
    # Container of this equipment.
    EquipmentContainer_: Optional[EquipmentContainer] = None
     