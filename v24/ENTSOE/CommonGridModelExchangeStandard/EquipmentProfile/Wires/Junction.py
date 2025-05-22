from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.Connector import Connector

@dataclass
class Junction(Connector):
    """A point where one or more conducting equipments are connected with zero
    resistance.
    """
    pass
