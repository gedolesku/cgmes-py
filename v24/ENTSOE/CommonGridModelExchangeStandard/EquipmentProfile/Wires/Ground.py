from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class Ground(ConductingEquipment):
    """A point where the system is grounded used for connecting conducting equipment
    to ground. The power system model can have any number of grounds.
    """
    pass
