from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ApparentPower import ApparentPower     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.OperationalLimit import OperationalLimit

@dataclass
class ApparentPowerLimit(OperationalLimit):
    """Apparent power limit.
    """
    # The apparent power limit.
    value: ApparentPower  = None
     