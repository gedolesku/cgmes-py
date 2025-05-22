from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCSwitch(DCConductingEquipment):
    """A switch within the DC system.
    """
    pass
