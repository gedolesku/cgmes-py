from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.AsynchronousMachineKind import AsynchronousMachineKind     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.RotatingMachine import RotatingMachine

@dataclass
class AsynchronousMachine(RotatingMachine):
    """A rotating machine whose shaft rotates asynchronously with the electrical field.
     Also known as an induction machine with no external connection to the rotor
    windings, e.g squirrel-cage induction machine.
    """
    # Indicates the type of Asynchronous Machine (motor or generator).
    asynchronousMachineType_: AsynchronousMachineKind  = None
     