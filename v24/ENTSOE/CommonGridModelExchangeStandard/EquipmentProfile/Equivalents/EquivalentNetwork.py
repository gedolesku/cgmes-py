from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Equivalents.EquivalentEquipment import EquivalentEquipment     

@dataclass
class EquivalentNetwork(ConnectivityNodeContainer):
    """A class that represents an external meshed network that has been reduced to an
    electrically equivalent model. The ConnectivityNodes contained in the
    equivalent are intended to reflect internal nodes of the equivalent. The
    boundary Connectivity nodes where the equivalent connects outside itself are
    NOT contained by the equivalent.
    """
    # The equivalent where the reduced model belongs.
    EquivalentEquipment_: List[EquivalentEquipment]  = field(default_factory=list)
     