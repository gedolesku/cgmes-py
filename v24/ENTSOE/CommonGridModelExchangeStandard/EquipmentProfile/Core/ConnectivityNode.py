from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Terminal import Terminal     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConnectivityNodeContainer import ConnectivityNodeContainer     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class ConnectivityNode(IdentifiedObject):
    """Connectivity nodes are points where terminals of AC conducting equipment are
    connected together with zero impedance.
    """
    # The connectivity node to which this terminal connects with zero impedance.
    Terminal_: List[Terminal]  = field(default_factory=list)
 
    # Container of this connectivity node.
    ConnectivityNodeContainer_: Optional[ConnectivityNodeContainer] = None
     