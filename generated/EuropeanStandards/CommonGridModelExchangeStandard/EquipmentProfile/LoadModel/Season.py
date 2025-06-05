from __future__ import annotations
from ...DomainProfile.MonthDay import MonthDay
from ..Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Season(IdentifiedObject):
    endDate: MonthDay = field(metadata={'xpath': 'cim:Season.endDate'})
    startDate: MonthDay = field(metadata={'xpath': 'cim:Season.startDate'})
