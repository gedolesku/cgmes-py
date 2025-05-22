from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.MonthDay import MonthDay     

@dataclass
class MonthDayInterval:
    """Interval between two times specified as mont and date.
    """
    # End time of this interval.
    end: MonthDay  = None
 
    # Start time of this interval.
    start: MonthDay  = None
     