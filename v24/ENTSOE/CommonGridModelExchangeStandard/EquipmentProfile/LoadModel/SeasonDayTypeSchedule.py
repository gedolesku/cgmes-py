from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.RegularIntervalSchedule import RegularIntervalSchedule
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.Season import Season     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.DayType import DayType     

@dataclass
class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """A time schedule covering a 24 hour period, with curve data for a specific type
    of season and day.
    """
    # Schedules that use this Season.
    Season_ref: Optional[Season] = None
    Season: str = None
 
    # Schedules that use this DayType.
    DayType_ref: Optional[DayType] = None
    DayType: str = None
     