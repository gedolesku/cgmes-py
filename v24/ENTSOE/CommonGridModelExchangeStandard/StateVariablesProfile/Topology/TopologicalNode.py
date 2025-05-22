from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

@dataclass
class TopologicalNode:
    """For a detailed substation model a topological node is a set of connectivity
    nodes that, in the current network state, are connected together through any
    type of closed switches, including  jumpers. Topological nodes change as the
    current network state changes (i.e., switches, breakers, etc. change state).
      For a planning model, switch statuses are not used to form topological nodes.
    Instead they are manually created or deleted in a model builder tool.
    Topological nodes maintained this way are also called "busses".
    """
    pass
