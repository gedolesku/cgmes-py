from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValue import MeasurementValue
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Accumulator import Accumulator     

@dataclass
class AccumulatorValue(MeasurementValue):
    """AccumulatorValue represents an accumulated (counted) MeasurementValue.
    """
    # The value to supervise. The value is positive.
    value_: int  = None
 
    # The values connected to this measurement.
    Accumulator_: Optional[Accumulator] = None
     