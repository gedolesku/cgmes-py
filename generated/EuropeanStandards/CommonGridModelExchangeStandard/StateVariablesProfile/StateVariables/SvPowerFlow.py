from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ReactivePower import ReactivePower
from ..Core.Terminal import Terminal
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SvPowerFlow:
    p: ActivePower = field(metadata={'xpath': 'cim:SvPowerFlow.p'})
    q: ReactivePower = field(metadata={'xpath': 'cim:SvPowerFlow.q'})
    Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:SvPowerFlow.Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Terminal_ref: Terminal = None
