from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.DateTime import DateTime     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time.
    """
    # The time for the first time point.
    startTime: DateTime  = None
 
    # Value1 units of measure.
    value1Unit: UnitSymbol  = None
 
    # Value2 units of measure.
    value2Unit: UnitSymbol  = None
     