from __future__ import annotations
from .ConnectivityNodeContainer import ConnectivityNodeContainer
from .IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ConnectivityNode(IdentifiedObject):
    ConnectivityNodeContainer_id: str | None = field(default=None, metadata={"xpath": "cim:ConnectivityNode.ConnectivityNodeContainer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConnectivityNodeContainer_ref: ConnectivityNodeContainer = None
