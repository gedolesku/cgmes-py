from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.OperationalLimitType import OperationalLimitType     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class OperationalLimit(IdentifiedObject):
    """A value associated with a specific kind of limit.
      The sub class value attribute shall be positive.
      The sub class value attribute is inversely proportional to
    OperationalLimitType.acceptableDuration (acceptableDuration for short). A pair
    of value_x and acceptableDuration_x are related to each other as follows:
      if value_1 > value_2 > value_3 >... then
      acceptableDuration_1 < acceptableDuration_2 < acceptableDuration_3 < ...
      A value_x with direction="high" shall be greater than a value_y with
    direction="low".
    """
    # The limit type associated with this limit.
    OperationalLimitType_ref: Optional[OperationalLimitType] = None
    OperationalLimitType: str = None
     