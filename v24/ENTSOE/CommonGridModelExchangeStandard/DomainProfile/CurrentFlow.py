from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class CurrentFlow:
    """Electrical current with sign convention: positive flow is out of the conducting
    equipment into the connectivity node. Can be both AC and DC.
    """
    value_: float  = None
 
    unit_: UnitSymbol =  UnitSymbol.A
 
    multiplier_: UnitMultiplier =  UnitMultiplier.none
     