from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.AnalogLimitSet import AnalogLimitSet     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Limit import Limit

@dataclass
class AnalogLimit(Limit):
    """Limit values for Analog measurements.
    """
    # The value to supervise against.
    value_: Simple_Float  = None
 
    # The limit values used for supervision of Measurements.
    AnalogLimitSet_: Optional[AnalogLimitSet] = None
     