from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class OverexcLimX2(OverexcitationLimiterDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:OverexcLimX2.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:OverexcLimX2.efd2'})
    efd3: PU = field(metadata={'xpath': 'cim:OverexcLimX2.efd3'})
    efddes: PU = field(metadata={'xpath': 'cim:OverexcLimX2.efddes'})
    efdrated: PU = field(metadata={'xpath': 'cim:OverexcLimX2.efdrated'})
    kmx: PU = field(metadata={'xpath': 'cim:OverexcLimX2.kmx'})
    m: Boolean = field(metadata={'xpath': 'cim:OverexcLimX2.m'})
    t1: Seconds = field(metadata={'xpath': 'cim:OverexcLimX2.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:OverexcLimX2.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:OverexcLimX2.t3'})
    vlow: PU = field(metadata={'xpath': 'cim:OverexcLimX2.vlow'})
