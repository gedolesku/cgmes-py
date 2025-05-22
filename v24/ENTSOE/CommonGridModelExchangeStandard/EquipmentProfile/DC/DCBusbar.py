from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCBusbar(DCConductingEquipment):
    """A busbar within a DC system.
    """
    pass
