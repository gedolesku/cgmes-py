from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class PerCent:
    """Percentage on a defined base.   For example, specify as 100 to indicate at the
    defined base.
    """
    # Normally 0 - 100 on a defined base
    value_: float  = None
 
    unit_: UnitSymbol =  UnitSymbol.none
 
    multiplier_: UnitMultiplier =  UnitMultiplier.none
     