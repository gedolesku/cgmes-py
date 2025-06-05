from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Simple_Float import Simple_Float
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class OverexcLimIEEE(OverexcitationLimiterDynamics):
    hyst: PU = field(metadata={'xpath': 'cim:OverexcLimIEEE.hyst'})
    ifdlim: PU = field(metadata={'xpath': 'cim:OverexcLimIEEE.ifdlim'})
    ifdmax: PU = field(metadata={'xpath': 'cim:OverexcLimIEEE.ifdmax'})
    itfpu: PU = field(metadata={'xpath': 'cim:OverexcLimIEEE.itfpu'})
    kcd: PU = field(metadata={'xpath': 'cim:OverexcLimIEEE.kcd'})
    kramp: Simple_Float = field(metadata={'xpath': 'cim:OverexcLimIEEE.kramp'})
