from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.AccumulatorLimitSet import AccumulatorLimitSet     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Limit import Limit

@dataclass
class AccumulatorLimit(Limit):
    """Limit values for Accumulator measurements.
    """
    # The value to supervise against. The value is positive.
    value: int  = None
 
    # The limit values used for supervision of Measurements.
    LimitSet_ref: Optional[AccumulatorLimitSet] = None
    LimitSet: str = None
     