from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class RegulatingCondEq(ConductingEquipment):
    """A type of conducting equipment that can regulate a quantity (i.e. voltage or
    flow) at a specific point in the network.
    """
    pass
