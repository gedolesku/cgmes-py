from __future__ import annotations
from ...StateVariablesProfile.Core.Terminal import Terminal
from ..Topology.TopologicalNode import TopologicalNode
from dataclasses import dataclass, field
# pylint: disable=function-redefined

@dataclass(kw_only=True)
class Terminal(Terminal):
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:Terminal.TopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNode_ref: TopologicalNode = None
