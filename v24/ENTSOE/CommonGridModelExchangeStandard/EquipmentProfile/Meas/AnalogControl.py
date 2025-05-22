from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.AnalogValue import AnalogValue     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Control import Control

@dataclass
class AnalogControl(Control):
    """An analog control used for supervisory control.
    """
    # Normal value range maximum for any of the Control.value. Used for scaling, e.g.
    # in bar graphs.
    maxValue_: Simple_Float  = None
 
    # Normal value range minimum for any of the Control.value. Used for scaling, e.g.
    # in bar graphs.
    minValue_: Simple_Float  = None
 
    # The Control variable associated with the MeasurementValue.
    AnalogValue_: Optional[AnalogValue] = None
     