from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .TopologicalNode import TopologicalNode
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class TopologicalIsland(IdentifiedObject):
    AngleRefTopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalIsland.AngleRefTopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    AngleRefTopologicalNode_ref: TopologicalNode = None
    TopologicalNodes_id: list[str] | None = field(default_factory=list, metadata={"xpath": "cim:TopologicalIsland.TopologicalNodes/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNodes_ref: TopologicalNode = None
