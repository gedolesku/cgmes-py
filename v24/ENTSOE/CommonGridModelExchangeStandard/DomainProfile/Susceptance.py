from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class Susceptance:
    """Imaginary part of admittance.
    """
    value_: float  = None
 
    unit_: UnitSymbol =  UnitSymbol.S
 
    multiplier_: UnitMultiplier =  UnitMultiplier.none
     