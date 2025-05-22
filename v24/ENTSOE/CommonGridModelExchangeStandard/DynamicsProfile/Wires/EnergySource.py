from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class EnergySource(ConductingEquipment):
    """A generic equivalent for an energy supplier on a transmission or distribution
    voltage level.
    """
    pass
