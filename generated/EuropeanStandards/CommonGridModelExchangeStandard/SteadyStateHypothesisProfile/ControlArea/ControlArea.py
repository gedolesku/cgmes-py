from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ..Core.PowerSystemResource import PowerSystemResource
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ControlArea(PowerSystemResource):
    netInterchange: ActivePower = field(metadata={'xpath': 'cim:ControlArea.netInterchange'})
    pTolerance: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:ControlArea.pTolerance'})
