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
    denominatorMultiplier_: UnitMultiplier =  UnitMultiplier.none
 
    denominatorUnit_: UnitSymbol =  UnitSymbol.Hz
 
    multiplier_: UnitMultiplier =  UnitMultiplier.M
 
    unit_: UnitSymbol =  UnitSymbol.W
 
    value_: float  = None
     