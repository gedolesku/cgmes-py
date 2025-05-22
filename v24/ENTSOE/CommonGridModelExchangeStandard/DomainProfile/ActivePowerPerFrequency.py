from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     

@dataclass
class ActivePowerPerFrequency:
    """Active power variation with frequency.
    """
    denominatorMultiplier: UnitMultiplier =  UnitMultiplier.none
 
    denominatorUnit: UnitSymbol =  UnitSymbol.Hz
 
    multiplier: UnitMultiplier =  UnitMultiplier.M
 
    unit: UnitSymbol =  UnitSymbol.W
 
    value: float  = None
     