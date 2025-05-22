from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.RegulatingControl import RegulatingControl

@dataclass
class TapChangerControl(RegulatingControl):
    """Describes behavior specific to tap changers, e.g. how the voltage at the end of
    a line varies with the load level and compensation of the voltage drop by tap
    adjustment.
    """
    pass
