from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Analog import Analog     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.LimitSet import LimitSet

@dataclass
class AnalogLimitSet(LimitSet):
    """An AnalogLimitSet specifies a set of Limits that are associated with an Analog
    measurement.
    """
    # A measurement may have zero or more limit ranges defined for it.
    Measurements: List[Analog]  = field(default_factory=list)
     