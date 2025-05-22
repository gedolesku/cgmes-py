from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.ConformLoadGroup import ConformLoadGroup     

@dataclass
class ConformLoadSchedule(SeasonDayTypeSchedule):
    """A curve of load  versus time (X-axis) showing the active power values (Y1-axis)
    and reactive power (Y2-axis) for each unit of the period covered. This curve
    represents a typical pattern of load over the time period for a given day type
    and season.
    """
    # The ConformLoadGroup where the ConformLoadSchedule belongs.
    ConformLoadGroup_: Optional[ConformLoadGroup] = None
     