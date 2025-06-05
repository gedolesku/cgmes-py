from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    kuc: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.kuc'})
    kuf: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.kuf'})
    kui: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.kui'})
    kul: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.kul'})
    kur: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.kur'})
    tu1: Seconds = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.tu1'})
    tu2: Seconds = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.tu2'})
    tu3: Seconds = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.tu3'})
    tu4: Seconds = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.tu4'})
    vucmax: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.vucmax'})
    vuimax: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.vuimax'})
    vuimin: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.vuimin'})
    vulmax: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.vulmax'})
    vulmin: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.vulmin'})
    vurmax: PU = field(metadata={'xpath': 'cim:UnderexcLimIEEE1.vurmax'})
