from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DayType(IdentifiedObject):
    """Group of similar days.   For example it could be used to represent weekdays,
    weekend, or holidays.
    """
    pass
