from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingControl import RegulatingControl     

@dataclass
class RegulationSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a controlled variable, e.g., busbar
    voltage.
    """
    # Regulating controls that have this Schedule.
    RegulatingControl_ref: Optional[RegulatingControl] = None
    RegulatingControl: str = None
     