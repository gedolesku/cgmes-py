from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValue import MeasurementValue
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.StringMeasurement import StringMeasurement     

@dataclass
class StringMeasurementValue(MeasurementValue):
    """StringMeasurementValue represents a measurement value of type string.
    """
    # The value to supervise.
    value: str  = None
 
    # Measurement to which this value is connected.
    StringMeasurement_ref: Optional[StringMeasurement] = None
    StringMeasurement: str = None
     