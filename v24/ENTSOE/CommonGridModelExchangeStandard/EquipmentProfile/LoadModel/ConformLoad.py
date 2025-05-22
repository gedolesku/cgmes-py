from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.ConformLoadGroup import ConformLoadGroup     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.EnergyConsumer import EnergyConsumer

@dataclass
class ConformLoad(EnergyConsumer):
    """ConformLoad represent loads that follow a daily load change pattern where the
    pattern can be used to scale the load with a system load.
    """
    # Group of this ConformLoad.
    ConformLoadGroup_: Optional[ConformLoadGroup] = None
     