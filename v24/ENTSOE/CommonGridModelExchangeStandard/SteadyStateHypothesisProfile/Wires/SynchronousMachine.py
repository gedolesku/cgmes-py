from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.SynchronousMachineOperatingMode import SynchronousMachineOperatingMode     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.RotatingMachine import RotatingMachine

@dataclass
class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates with shaft rotating synchronously
    with the network. It is a single machine operating either as a generator or
    synchronous condenser or pump.
    """
    # Current mode of operation.
    operatingMode_: SynchronousMachineOperatingMode  = None
     