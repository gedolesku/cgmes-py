from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Currency import Currency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Decimal import Decimal     

@dataclass
class Money:
    """Amount of money.
    """
    unit: Currency =  Currency.EUR
 
    multiplier: UnitMultiplier =  UnitMultiplier.none
 
    value: Decimal  = None
     