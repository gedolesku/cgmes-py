from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.DC.ACDCConverter import ACDCConverter

@dataclass
class CsConverter(ACDCConverter):
    """DC side of the current source converter (CSC).
    """
    # Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC
    # state variable, result from power flow.
    alpha: AngleDegrees  = None
 
    # Extinction angle. CSC state variable, result from power flow.
    gamma: AngleDegrees  = None
     