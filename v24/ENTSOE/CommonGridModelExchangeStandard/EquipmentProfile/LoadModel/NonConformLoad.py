from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.NonConformLoadGroup import NonConformLoadGroup     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.EnergyConsumer import EnergyConsumer

@dataclass
class NonConformLoad(EnergyConsumer):
    """NonConformLoad represent loads that do not follow a daily load change pattern
    and changes are not correlated with the daily load change pattern.
    """
    # Conform loads assigned to this ConformLoadGroup.
    NonConformLoadGroup_: Optional[NonConformLoadGroup] = None
     