from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.OperationalLimit import OperationalLimit

@dataclass
class CurrentLimit(OperationalLimit):
    """Operational limit on current.
    """
    # Limit on current flow.
    value_: CurrentFlow  = None
     