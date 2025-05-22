from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.AnalogControl import AnalogControl

@dataclass
class SetPoint(AnalogControl):
    """An analog control that issue a set point value.
    """
    # Normal value for Control.value e.g. used for percentage scaling.
    normalValue: Simple_Float  = None
 
    # The value representing the actuator output.
    value: Simple_Float  = None
     