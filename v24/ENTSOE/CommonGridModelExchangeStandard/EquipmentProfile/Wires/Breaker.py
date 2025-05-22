from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.ProtectedSwitch import ProtectedSwitch

@dataclass
class Breaker(ProtectedSwitch):
    """A mechanical switching device capable of making, carrying, and breaking
    currents under normal circuit conditions and also making, carrying for a
    specified time, and breaking currents under specified abnormal circuit
    conditions e.g.  those of short circuit.
    """
    pass
