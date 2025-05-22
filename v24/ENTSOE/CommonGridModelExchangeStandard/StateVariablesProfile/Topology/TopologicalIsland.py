from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Topology.TopologicalNode import TopologicalNode     

@dataclass
class TopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. Topological islands can change
    as the current network state changes: e.g. due to
      - disconnect switches or breakers change state in a SCADA/EMS
      - manual creation, change or deletion of topological nodes in a planning tool.
    """
    # The angle reference for the island.   Normally there is one TopologicalNode
    # that is selected as the angle reference for each island.   Other reference
    # schemes exist, so the association is typically optional.
    TopologicalNode_: Optional[TopologicalNode] = None
 
    # A topological node belongs to a topological island.
    TopologicalNode_: List[TopologicalNode]  = field(default_factory=list)
     