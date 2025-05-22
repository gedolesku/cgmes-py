from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TapChanger import TapChanger     

@dataclass
class TapSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a tap step.
    """
    # A TapChanger can have TapSchedules.
    TapChanger_: Optional[TapChanger] = None
     