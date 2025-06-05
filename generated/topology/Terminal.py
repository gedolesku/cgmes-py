"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from .IdentifiedObject import IdentifiedObject

__all__ = ['Terminal']

@dataclass(kw_only=True)
class Terminal(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:Terminal.TopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNode_ref: 'TopologicalNode' | None = None
