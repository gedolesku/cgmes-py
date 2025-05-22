from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Equipment import Equipment     

@dataclass
class EquipmentContainer(ConnectivityNodeContainer):
    """A modeling construct to provide a root class for containing equipment.
    """
    # Contained equipment.
    Equipment_: List[Equipment]  = field(default_factory=list)
     