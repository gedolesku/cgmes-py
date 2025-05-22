from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Generation.GeneratingUnit import GeneratingUnit

@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover is a hydraulic turbine (e.g., Francis,
    Pelton, Kaplan).
    """
    pass
