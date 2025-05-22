from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.DC.DCTopologicalNode import DCTopologicalNode     
from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DCNode(IdentifiedObject):
    """DC nodes are points where terminals of DC conducting equipment are connected
    together with zero impedance.
    """
    # See association end TopologicalNode.ConnectivityNodes.
    DCTopologicalNode_ref: Optional[DCTopologicalNode] = None
    DCTopologicalNode: str = None
     