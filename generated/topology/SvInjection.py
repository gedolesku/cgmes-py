"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List
from .IdentifiedObject import IdentifiedObject

__all__ = ['SvInjection']

@dataclass(kw_only=True)
class SvInjection(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    pInjection: ActivePower = field(metadata={'xpath': 'cim:SvInjection.pInjection'})
    qInjection: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:SvInjection.qInjection'})
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:SvInjection.TopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNode_ref: 'TopologicalNode' | None = None
