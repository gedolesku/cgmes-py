from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Wires.RotatingMachine import RotatingMachine

@dataclass
class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates with shaft rotating synchronously
    with the network. It is a single machine operating either as a generator or
    synchronous condenser or pump.
    """
    pass
