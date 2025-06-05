from __future__ import annotations
from ..Topology.TopologicalNode import TopologicalNode
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ConnectivityNode:
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:ConnectivityNode.TopologicalNode/@rdf:resource", "pattern": r"^#.+$"})
    TopologicalNode_ref: TopologicalNode | None = None
