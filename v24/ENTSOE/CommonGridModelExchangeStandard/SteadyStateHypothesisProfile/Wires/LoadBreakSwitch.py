from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.ProtectedSwitch import ProtectedSwitch

@dataclass
class LoadBreakSwitch(ProtectedSwitch):
    """A mechanical switching device capable of making, carrying, and breaking
    currents under normal operating conditions.
    """
    pass
