from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.NonConformLoadGroup import NonConformLoadGroup     

@dataclass
class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus
    time (X-axis) for non-conforming loads, e.g., large industrial load or power
    station service (where modeled).
    """
    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    NonConformLoadGroup_: Optional[NonConformLoadGroup] = None
     