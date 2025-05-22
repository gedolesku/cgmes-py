from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.Switch import Switch     

@dataclass
class SwitchSchedule(SeasonDayTypeSchedule):
    """A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is
    open.  If 1, the switch is closed.
    """
    # A Switch can be associated with SwitchSchedules.
    Switch_: Optional[Switch] = None
     