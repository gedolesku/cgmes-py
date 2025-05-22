from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     
if TYPE_CHECKING:          from TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from TC57CIM.IEC61970.Base.Domain.Float import Float     

@dataclass
class ActivePowerPerCurrentFlow:
    denominatorMultiplier: UnitMultiplier =  UnitMultiplier.none
 
    denominatorUnit: UnitSymbol =  UnitSymbol.A
 
    multiplier: UnitMultiplier =  UnitMultiplier.M
 
    unit: UnitSymbol =  UnitSymbol.W
 
    value: float  = None
     