from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class ActivePower:
    """Product of RMS value of the voltage and the RMS value of the in-phase component
    of the current.
    """
    value: float  = None
 
    unit: UnitSymbol =  UnitSymbol.W
 
    multiplier: UnitMultiplier =  UnitMultiplier.M
     