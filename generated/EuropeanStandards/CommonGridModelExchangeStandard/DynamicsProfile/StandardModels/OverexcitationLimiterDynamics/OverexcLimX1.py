from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class OverexcLimX1(OverexcitationLimiterDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:OverexcLimX1.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:OverexcLimX1.efd2'})
    efd3: PU = field(metadata={'xpath': 'cim:OverexcLimX1.efd3'})
    efddes: PU = field(metadata={'xpath': 'cim:OverexcLimX1.efddes'})
    efdrated: PU = field(metadata={'xpath': 'cim:OverexcLimX1.efdrated'})
    kmx: PU = field(metadata={'xpath': 'cim:OverexcLimX1.kmx'})
    t1: Seconds = field(metadata={'xpath': 'cim:OverexcLimX1.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:OverexcLimX1.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:OverexcLimX1.t3'})
    vlow: PU = field(metadata={'xpath': 'cim:OverexcLimX1.vlow'})
