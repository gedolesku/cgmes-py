from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.ConductingEquipment import ConductingEquipment
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Wires.EnergySchedulingType import EnergySchedulingType     

@dataclass
class EnergySource(ConductingEquipment):
    """A generic equivalent for an energy supplier on a transmission or distribution
    voltage level.
    """
    # Energy Scheduling Type of an Energy Source
    EnergySchedulingType_ref: Optional[EnergySchedulingType] = None
    EnergySchedulingType: str = None
     