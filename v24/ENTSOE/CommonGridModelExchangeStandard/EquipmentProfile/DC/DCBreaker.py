from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCSwitch import DCSwitch

@dataclass
class DCBreaker(DCSwitch):
    """A breaker within a DC system.
    """
    pass
