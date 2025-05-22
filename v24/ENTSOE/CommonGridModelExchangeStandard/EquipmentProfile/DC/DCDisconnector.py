from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCSwitch import DCSwitch

@dataclass
class DCDisconnector(DCSwitch):
    """A disconnector within a DC system.
    """
    pass
