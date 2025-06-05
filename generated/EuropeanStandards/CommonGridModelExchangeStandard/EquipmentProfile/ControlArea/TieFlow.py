from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..Core.Terminal import Terminal
from .ControlArea import ControlArea
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TieFlow:
    positiveFlowIn: Boolean = field(metadata={'xpath': 'cim:TieFlow.positiveFlowIn'})
    ControlArea_id: str | None = field(default=None, metadata={"xpath": "cim:TieFlow.ControlArea/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ControlArea_ref: ControlArea = None
    Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:TieFlow.Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Terminal_ref: Terminal = None
