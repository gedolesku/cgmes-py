from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.LimitSet import LimitSet
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Accumulator import Accumulator     

@dataclass
class AccumulatorLimitSet(LimitSet):
    """An AccumulatorLimitSet specifies a set of Limits that are associated with an
    Accumulator measurement.
    """
    # A measurement may have zero or more limit ranges defined for it.
    Accumulator_: List[Accumulator]  = field(default_factory=list)
     