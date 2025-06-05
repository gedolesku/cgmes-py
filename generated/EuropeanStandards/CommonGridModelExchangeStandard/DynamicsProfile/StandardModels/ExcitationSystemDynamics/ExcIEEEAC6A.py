from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC6A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.ke'})
    kh: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.kh'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC6A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC6A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.te'})
    th: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.th'})
    tj: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.tj'})
    tk: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC6A.tk'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.ve2'})
    vfelim: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.vfelim'})
    vhmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.vhmax'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC6A.vrmin'})
