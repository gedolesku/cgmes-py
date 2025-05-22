from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import TopologicalNode     

@dataclass
class ConnectivityNode:
    """Connectivity nodes are points where terminals of AC conducting equipment are
    connected together with zero impedance.
    """
    # The connectivity nodes combine together to form this topological node.  May
    # depend on the current state of switches in the network.
    TopologicalNode_: Optional[TopologicalNode] = None
     