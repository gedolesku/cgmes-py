from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanical.
    """
    pass
