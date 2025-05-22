from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Generation.GeneratingUnit import GeneratingUnit

@dataclass
class SolarGeneratingUnit(GeneratingUnit):
    """A solar thermal generating unit.
    """
    pass
