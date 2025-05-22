from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.ConformLoadSchedule import ConformLoadSchedule     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.LoadGroup import LoadGroup
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.ConformLoad import ConformLoad     

@dataclass
class ConformLoadGroup(LoadGroup):
    """A group of loads conforming to an allocation pattern.
    """
    # The ConformLoadSchedules in the ConformLoadGroup.
    ConformLoadSchedule_: List[ConformLoadSchedule]  = field(default_factory=list)
 
    # Conform loads assigned to this ConformLoadGroup.
    ConformLoad_: List[ConformLoad]  = field(default_factory=list)
     