from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.DC.DCTopologicalNode import DCTopologicalNode     
from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.ACDCTerminal import ACDCTerminal

@dataclass
class DCBaseTerminal(ACDCTerminal):
    """An electrical connection point at a piece of DC conducting equipment. DC
    terminals are connected at one physical DC node that may have multiple DC
    terminals connected. A DC node is similar to an AC connectivity node. The model
    enforces that DC connections are distinct from AC connections.
    """
    # See association end TopologicalNode.Terminal.
    DCTopologicalNode_ref: Optional[DCTopologicalNode] = None
    DCTopologicalNode: str = None
     