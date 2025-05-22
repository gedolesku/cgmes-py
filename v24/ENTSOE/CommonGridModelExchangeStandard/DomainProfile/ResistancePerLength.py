from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     

@dataclass
class ResistancePerLength:
    """Resistance (real part of impedance) per unit of length.
    """
    value: float  = None
 
    unit: UnitSymbol =  UnitSymbol.ohm
 
    multiplier: UnitMultiplier =  UnitMultiplier.none
 
    denominatorUnit: UnitSymbol =  UnitSymbol.m
 
    denominatorMultiplier: UnitMultiplier =  UnitMultiplier.none
     