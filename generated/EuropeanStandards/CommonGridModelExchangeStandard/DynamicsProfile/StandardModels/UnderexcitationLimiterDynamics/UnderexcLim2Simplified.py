from __future__ import annotations
from ....DomainProfile.PU import PU
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    kui: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.kui'})
    p0: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.p0'})
    p1: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.p1'})
    q0: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.q0'})
    q1: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.q1'})
    vuimax: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.vuimax'})
    vuimin: PU = field(metadata={'xpath': 'cim:UnderexcLim2Simplified.vuimin'})
