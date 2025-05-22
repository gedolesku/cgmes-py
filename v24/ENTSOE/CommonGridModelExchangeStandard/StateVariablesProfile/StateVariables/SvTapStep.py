from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Wires.TapChanger import TapChanger     

@dataclass
class SvTapStep:
    """State variable for transformer tap step.     This class is to be used for taps
    of LTC (load tap changing) transformers, not fixed tap transformers.
    """
    # The floating point tap position.   This is not the tap ratio, but rather the
    # tap step position as defined by the related tap changer model and normally is
    # constrained to be within the range of minimum and maximum tap positions.
    position_: Simple_Float  = None
 
    # The tap changer associated with the tap step state.
    TapChanger_: Optional[TapChanger] = None
     