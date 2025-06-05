"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from .IdentifiedObject import IdentifiedObject

__all__ = ['SvTapStep']

@dataclass(kw_only=True)
class SvTapStep(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    position: Simple_Float = field(metadata={'xpath': 'cim:SvTapStep.position'})
    TapChanger_id: str | None = field(default=None, metadata={"xpath": "cim:SvTapStep.TapChanger/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TapChanger_ref: 'TapChanger' | None = None
