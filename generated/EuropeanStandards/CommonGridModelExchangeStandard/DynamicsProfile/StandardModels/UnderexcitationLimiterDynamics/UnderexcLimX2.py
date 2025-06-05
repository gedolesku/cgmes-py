from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class UnderexcLimX2(UnderexcitationLimiterDynamics):
    kf2: PU = field(metadata={'xpath': 'cim:UnderexcLimX2.kf2'})
    km: PU = field(metadata={'xpath': 'cim:UnderexcLimX2.km'})
    melmax: PU = field(metadata={'xpath': 'cim:UnderexcLimX2.melmax'})
    qo: PU = field(metadata={'xpath': 'cim:UnderexcLimX2.qo'})
    r: PU = field(metadata={'xpath': 'cim:UnderexcLimX2.r'})
    tf2: Seconds = field(metadata={'xpath': 'cim:UnderexcLimX2.tf2'})
    tm: Seconds = field(metadata={'xpath': 'cim:UnderexcLimX2.tm'})
