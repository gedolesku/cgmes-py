from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .DCTopologicalNode import DCTopologicalNode
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCNode(IdentifiedObject):
    DCTopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:DCNode.DCTopologicalNode/@rdf:resource", "pattern": r"^#.+$"})
    DCTopologicalNode_ref: DCTopologicalNode | None = None
