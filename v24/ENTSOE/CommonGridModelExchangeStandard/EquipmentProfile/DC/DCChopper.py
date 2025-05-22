from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCChopper(DCConductingEquipment):
    """Low resistance equipment used in the internal DC circuit to balance voltages.
    It has typically positive and negative pole terminals and a ground.
    """
    pass
