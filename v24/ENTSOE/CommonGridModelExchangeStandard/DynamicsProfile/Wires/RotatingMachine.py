from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class RotatingMachine(RegulatingCondEq):
    """A rotating machine which may be used as a generator or motor.
    """
    pass
