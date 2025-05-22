from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class VoltagePerReactivePower:
    """Voltage variation with reactive power.
    """
    value: float  = None
 
    unit: UnitSymbol =  UnitSymbol.V
 
    denominatorMultiplier: UnitMultiplier =  UnitMultiplier.M
 
    multiplier: UnitMultiplier =  UnitMultiplier.k
 
    denominatorUnit: UnitSymbol =  UnitSymbol.VAr
     