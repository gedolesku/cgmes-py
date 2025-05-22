from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.TapChanger import TapChanger

@dataclass
class PhaseTapChanger(TapChanger):
    """A transformer phase shifting tap model that controls the phase angle difference
    across the power transformer and potentially the active power flow through the
    power transformer.  This phase tap model may also impact the voltage magnitude.
    """
    pass
