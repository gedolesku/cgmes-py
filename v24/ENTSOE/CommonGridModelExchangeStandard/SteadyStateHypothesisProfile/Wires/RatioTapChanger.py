from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.TapChanger import TapChanger

@dataclass
class RatioTapChanger(TapChanger):
    """A tap changer that changes the voltage ratio impacting the voltage magnitude
    but not the phase angle across the transformer.
    """
    pass
