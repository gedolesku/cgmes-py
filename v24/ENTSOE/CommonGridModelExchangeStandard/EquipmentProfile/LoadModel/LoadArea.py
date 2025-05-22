from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SubLoadArea import SubLoadArea     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.EnergyArea import EnergyArea

@dataclass
class LoadArea(EnergyArea):
    """The class is the root or first level in a hierarchical structure for grouping
    of loads for the purpose of load flow load scaling.
    """
    # The SubLoadAreas in the LoadArea.
    SubLoadArea_: List[SubLoadArea]  = field(default_factory=list)
     