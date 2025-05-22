from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class PU:
    """Per Unit - a positive or negative value referred to a defined base. Values
    typically range from -10 to +10.
    """
    value: float  = None
 
    unit: UnitSymbol =  UnitSymbol.none
 
    multiplier: UnitMultiplier =  UnitMultiplier.none
     