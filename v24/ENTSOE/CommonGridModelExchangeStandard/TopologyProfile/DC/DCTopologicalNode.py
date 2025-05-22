from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.DC.DCEquipmentContainer import DCEquipmentContainer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.DC.DCBaseTerminal import DCBaseTerminal     

@dataclass
class DCTopologicalNode(IdentifiedObject):
    """DC bus.
    """
    DCEquipmentContainer_: Optional[DCEquipmentContainer] = None
 
    # See association end Terminal.TopologicalNode.
    DCBaseTerminal_: List[DCBaseTerminal]  = field(default_factory=list)
     