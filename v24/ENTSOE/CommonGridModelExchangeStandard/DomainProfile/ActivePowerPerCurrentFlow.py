from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     
if TYPE_CHECKING:          from TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from TC57CIM.IEC61970.Base.Domain.Float import Float     

@dataclass
class ActivePowerPerCurrentFlow:
    denominatorMultiplier_: UnitMultiplier =  UnitMultiplier.none
 
    denominatorUnit_: UnitSymbol =  UnitSymbol.A
 
    multiplier_: UnitMultiplier =  UnitMultiplier.M
 
    unit_: UnitSymbol =  UnitSymbol.W
 
    value_: float  = None
     