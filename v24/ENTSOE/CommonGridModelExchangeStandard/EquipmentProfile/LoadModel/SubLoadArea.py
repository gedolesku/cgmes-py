from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.EnergyArea import EnergyArea
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.LoadGroup import LoadGroup     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.LoadArea import LoadArea     

@dataclass
class SubLoadArea(EnergyArea):
    """The class is the second level in a hierarchical structure for grouping of loads
    for the purpose of load flow load scaling.
    """
    # The Loadgroups in the SubLoadArea.
    LoadGroup_: List[LoadGroup]  = field(default_factory=list)
 
    # The LoadArea where the SubLoadArea belongs.
    LoadArea_: Optional[LoadArea] = None
     