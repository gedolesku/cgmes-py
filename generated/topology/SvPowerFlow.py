"""Auto-generated — DO NOT EDIT BY HAND"""

from __future__ import annotations
from dataclasses import dataclass, field
from .IdentifiedObject import IdentifiedObject

__all__ = ['SvPowerFlow']

@dataclass(kw_only=True)
class SvPowerFlow(IdentifiedObject):
    """Auto-generated — DO NOT EDIT BY HAND"""
    p: ActivePower = field(metadata={'xpath': 'cim:SvPowerFlow.p'})
    q: ReactivePower = field(metadata={'xpath': 'cim:SvPowerFlow.q'})
    Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:SvPowerFlow.Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Terminal_ref: 'Terminal' | None = None
