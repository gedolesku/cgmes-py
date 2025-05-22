from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DCNode(IdentifiedObject):
    """DC nodes are points where terminals of DC conducting equipment are connected
    together with zero impedance.
    """
    pass
