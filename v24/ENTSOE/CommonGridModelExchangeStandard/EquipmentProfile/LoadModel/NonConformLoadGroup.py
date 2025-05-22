from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.NonConformLoadSchedule import NonConformLoadSchedule     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.LoadGroup import LoadGroup

@dataclass
class NonConformLoadGroup(LoadGroup):
    """Loads that do not follow a daily and seasonal load variation pattern.
    """
    # The NonConformLoadSchedules in the NonConformLoadGroup.
    NonConformLoadSchedule_: List[NonConformLoadSchedule]  = field(default_factory=list)
     