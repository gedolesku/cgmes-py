from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.OperationalLimit import OperationalLimit

@dataclass
class VoltageLimit(OperationalLimit):
    """Operational limit applied to voltage.
    """
    # Limit on voltage. High or low limit nature of the limit depends upon the
    # properties of the operational limit type.
    value_: Voltage  = None
     