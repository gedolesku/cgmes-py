from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Generation.GeneratingUnit import GeneratingUnit

@dataclass
class NuclearGeneratingUnit(GeneratingUnit):
    """A nuclear generating unit.
    """
    pass
