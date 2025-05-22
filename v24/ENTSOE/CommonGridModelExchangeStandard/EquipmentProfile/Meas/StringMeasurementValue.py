from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValue import MeasurementValue
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.StringMeasurement import StringMeasurement     

@dataclass
class StringMeasurementValue(MeasurementValue):
    """StringMeasurementValue represents a measurement value of type string.
    """
    # The value to supervise.
    value_: str  = None
 
    # Measurement to which this value is connected.
    StringMeasurement_: Optional[StringMeasurement] = None
     