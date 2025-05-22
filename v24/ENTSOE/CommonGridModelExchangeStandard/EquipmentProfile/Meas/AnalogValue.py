from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValue import MeasurementValue
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Analog import Analog     

@dataclass
class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue.
    """
    # The value to supervise.
    value_: Simple_Float  = None
 
    # The values connected to this measurement.
    Analog_: Optional[Analog] = None
     