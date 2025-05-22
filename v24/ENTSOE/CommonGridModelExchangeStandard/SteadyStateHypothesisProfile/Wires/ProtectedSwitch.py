from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.Switch import Switch

@dataclass
class ProtectedSwitch(Switch):
    """A ProtectedSwitch is a switching device that can be operated by
    ProtectionEquipment.
    """
    pass
