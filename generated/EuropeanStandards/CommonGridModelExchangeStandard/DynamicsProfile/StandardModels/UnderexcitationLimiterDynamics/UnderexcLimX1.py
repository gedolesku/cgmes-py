from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class UnderexcLimX1(UnderexcitationLimiterDynamics):
    k: PU = field(metadata={'xpath': 'cim:UnderexcLimX1.k'})
    kf2: PU = field(metadata={'xpath': 'cim:UnderexcLimX1.kf2'})
    km: PU = field(metadata={'xpath': 'cim:UnderexcLimX1.km'})
    melmax: PU = field(metadata={'xpath': 'cim:UnderexcLimX1.melmax'})
    tf2: Seconds = field(metadata={'xpath': 'cim:UnderexcLimX1.tf2'})
    tm: Seconds = field(metadata={'xpath': 'cim:UnderexcLimX1.tm'})
