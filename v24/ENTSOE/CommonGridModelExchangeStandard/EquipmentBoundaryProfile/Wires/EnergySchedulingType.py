from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Wires.EnergySource import EnergySource     

@dataclass
class EnergySchedulingType(IdentifiedObject):
    """Used to define the type of generation for scheduling purposes.
    """
    # Energy Source of a particular Energy Scheduling Type
    EnergySource_: List[EnergySource]  = field(default_factory=list)
     