from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.OperationalLimit import OperationalLimit

@dataclass
class ActivePowerLimit(OperationalLimit):
    """Limit on active power flow.
    """
    # Value of active power limit.
    value_: ActivePower  = None
     