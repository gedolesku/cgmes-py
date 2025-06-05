from __future__ import annotations
from ....DomainProfile.PU import PU
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class OverexcLim2(OverexcitationLimiterDynamics):
    ifdlim: PU = field(metadata={'xpath': 'cim:OverexcLim2.ifdlim'})
    koi: PU = field(metadata={'xpath': 'cim:OverexcLim2.koi'})
    voimax: PU = field(metadata={'xpath': 'cim:OverexcLim2.voimax'})
    voimin: PU = field(metadata={'xpath': 'cim:OverexcLim2.voimin'})
