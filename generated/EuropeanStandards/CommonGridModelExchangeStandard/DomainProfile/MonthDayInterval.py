from __future__ import annotations
from .MonthDay import MonthDay
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class MonthDayInterval:
    end: Optional[MonthDay] = field(default=None, metadata={'xpath': 'cim:MonthDayInterval.end'})
    start: Optional[MonthDay] = field(default=None, metadata={'xpath': 'cim:MonthDayInterval.start'})
