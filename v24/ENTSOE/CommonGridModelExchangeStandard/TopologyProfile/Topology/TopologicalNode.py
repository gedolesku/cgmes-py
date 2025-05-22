from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.ReportingGroup import ReportingGroup     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.ConnectivityNodeContainer import ConnectivityNodeContainer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.BaseVoltage import BaseVoltage     

@dataclass
class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a topological node is a set of connectivity
    nodes that, in the current network state, are connected together through any
    type of closed switches, including  jumpers. Topological nodes change as the
    current network state changes (i.e., switches, breakers, etc. change state).
      For a planning model, switch statuses are not used to form topological nodes.
    Instead they are manually created or deleted in a model builder tool.
    Topological nodes maintained this way are also called "busses".
    """
    # The topological nodes that belong to the reporting group.
    ReportingGroup_: Optional[ReportingGroup] = None
 
    # The connectivity node container to which the toplogical node belongs.
    ConnectivityNodeContainer_: Optional[ConnectivityNodeContainer] = None
 
    # The base voltage of the topologocial node.
    BaseVoltage_: Optional[BaseVoltage] = None
     