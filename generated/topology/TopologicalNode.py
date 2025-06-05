"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List
from .IdentifiedObject import IdentifiedObject

__all__ = ['TopologicalNode']

@dataclass(kw_only=True)
class TopologicalNode(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    BaseVoltage_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.BaseVoltage/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    BaseVoltage_ref: 'BaseVoltage' | None = None
    ConnectivityNodeContainer_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConnectivityNodeContainer_ref: 'ConnectivityNodeContainer' | None = None
    ReportingGroup_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.ReportingGroup/@rdf:resource", "pattern": r"^#.+$"})
    ReportingGroup_ref: 'ReportingGroup' | None = None
