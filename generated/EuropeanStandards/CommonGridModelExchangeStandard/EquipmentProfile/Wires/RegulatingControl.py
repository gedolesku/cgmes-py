from __future__ import annotations
from ..Core.PowerSystemResource import PowerSystemResource
from ..Core.Terminal import Terminal
from .RegulatingControlModeKind import RegulatingControlModeKind
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class RegulatingControl(PowerSystemResource):
    mode: RegulatingControlModeKind = field(metadata={'xpath': 'cim:RegulatingControl.mode'})
    Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:RegulatingControl.Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Terminal_ref: Terminal = None
