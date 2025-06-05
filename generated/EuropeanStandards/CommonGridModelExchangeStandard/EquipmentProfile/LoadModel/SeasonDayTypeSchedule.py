from __future__ import annotations
from ..Core.RegularIntervalSchedule import RegularIntervalSchedule
from .DayType import DayType
from .Season import Season
from typing import Protocol, runtime_checkable

@runtime_checkable
class SeasonDayTypeSchedule(RegularIntervalSchedule, Protocol):
    Season_ref: Season  # metadata: cim='cim:SeasonDayTypeSchedule.Season', mult='1'
    Season_id: str
    DayType_ref: DayType  # metadata: cim='cim:SeasonDayTypeSchedule.DayType', mult='1'
    DayType_id: str
