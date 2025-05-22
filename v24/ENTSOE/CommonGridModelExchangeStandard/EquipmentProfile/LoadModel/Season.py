from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.MonthDay import MonthDay     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class Season(IdentifiedObject):
    """A specified time period of the year.
    """
    # Date season ends.
    endDate_: MonthDay  = None
 
    # Date season starts.
    startDate_: MonthDay  = None
     