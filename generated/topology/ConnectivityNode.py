"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List
from .IdentifiedObject import IdentifiedObject

__all__ = ['ConnectivityNode']

@dataclass(kw_only=True)
class ConnectivityNode(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:ConnectivityNode.TopologicalNode/@rdf:resource", "pattern": r"^#.+$"})
    TopologicalNode_ref: 'TopologicalNode' | None = None
