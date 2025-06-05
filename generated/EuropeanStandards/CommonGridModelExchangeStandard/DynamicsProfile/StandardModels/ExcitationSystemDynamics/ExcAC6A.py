from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAC6A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcAC6A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcAC6A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcAC6A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcAC6A.ke'})
    kh: PU = field(metadata={'xpath': 'cim:ExcAC6A.kh'})
    ks: PU = field(metadata={'xpath': 'cim:ExcAC6A.ks'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcAC6A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcAC6A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.te'})
    th: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.th'})
    tj: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.tj'})
    tk: Seconds = field(metadata={'xpath': 'cim:ExcAC6A.tk'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcAC6A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcAC6A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcAC6A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcAC6A.ve2'})
    vfelim: PU = field(metadata={'xpath': 'cim:ExcAC6A.vfelim'})
    vhmax: PU = field(metadata={'xpath': 'cim:ExcAC6A.vhmax'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcAC6A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcAC6A.vrmin'})
