from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import TopologicalNode     
from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.ACDCTerminal import ACDCTerminal

@dataclass
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment. Terminals
    are connected at physical connection points called connectivity nodes.
    """
    # The terminals associated with the topological node.   This can be used as an
    # alternative to the connectivity node path to terminal, thus making it
    # unneccesary to model connectivity nodes in some cases.   Note that if
    # connectivity nodes are in the model, this association would probably not be
    # used as an input specification.
    TopologicalNode_ref: Optional[TopologicalNode] = None
    TopologicalNode: str = None
     