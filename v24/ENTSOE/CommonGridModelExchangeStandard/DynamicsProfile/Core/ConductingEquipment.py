from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.Equipment import Equipment

@dataclass
class ConductingEquipment(Equipment):
    """The parts of the AC power system that are designed to carry current or that are
    conductively connected through terminals.
    """
    pass
