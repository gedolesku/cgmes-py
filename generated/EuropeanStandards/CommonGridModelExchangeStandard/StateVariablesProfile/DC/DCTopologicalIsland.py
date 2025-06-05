from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from ..Topology.DCTopologicalNode import DCTopologicalNode
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCTopologicalIsland(IdentifiedObject):
    DCTopologicalNodes_id: list[str] | None = field(default_factory=list, metadata={"xpath": "cim:DCTopologicalIsland.DCTopologicalNodes/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    DCTopologicalNodes_ref: DCTopologicalNode = None
