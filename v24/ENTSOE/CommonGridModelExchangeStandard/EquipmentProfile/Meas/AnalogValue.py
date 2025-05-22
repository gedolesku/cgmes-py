from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValue import MeasurementValue
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Analog import Analog     

@dataclass
class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue.
    """
    # The value to supervise.
    value: Simple_Float  = None
 
    # The values connected to this measurement.
    Analog_ref: Optional[Analog] = None
    Analog: str = None
     