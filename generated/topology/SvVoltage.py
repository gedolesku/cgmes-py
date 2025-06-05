"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from .IdentifiedObject import IdentifiedObject

__all__ = ['SvVoltage']

@dataclass(kw_only=True)
class SvVoltage(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    angle: AngleDegrees = field(metadata={'xpath': 'cim:SvVoltage.angle'})
    v: Voltage = field(metadata={'xpath': 'cim:SvVoltage.v'})
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:SvVoltage.TopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNode_ref: 'TopologicalNode' | None = None
