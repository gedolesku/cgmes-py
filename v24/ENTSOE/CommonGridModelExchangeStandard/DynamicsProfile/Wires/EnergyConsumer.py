from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system model.
    """
    # Load dynamics model used to describe dynamic behavior of this energy consumer.
    LoadDynamics_: Optional[LoadDynamics] = None
     