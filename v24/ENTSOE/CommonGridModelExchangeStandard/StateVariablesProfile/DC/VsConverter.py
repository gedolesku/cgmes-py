from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.DC.ACDCConverter import ACDCConverter

@dataclass
class VsConverter(ACDCConverter):
    """DC side of the voltage source converter (VSC).
    """
    # Angle between uf and uc. Converter state variable used in power flow.
    delta_: AngleDegrees  = None
 
    # Filter bus voltage. Converter state variable, result from power flow.
    uf_: Voltage  = None
     