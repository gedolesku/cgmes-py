from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAC3A(ExcitationSystemDynamics):
    efdn: PU = field(metadata={'xpath': 'cim:ExcAC3A.efdn'})
    ka: Seconds = field(metadata={'xpath': 'cim:ExcAC3A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcAC3A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcAC3A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcAC3A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcAC3A.kf'})
    kf1: PU = field(metadata={'xpath': 'cim:ExcAC3A.kf1'})
    kf2: PU = field(metadata={'xpath': 'cim:ExcAC3A.kf2'})
    klv: PU = field(metadata={'xpath': 'cim:ExcAC3A.klv'})
    kn: PU = field(metadata={'xpath': 'cim:ExcAC3A.kn'})
    kr: PU = field(metadata={'xpath': 'cim:ExcAC3A.kr'})
    ks: PU = field(metadata={'xpath': 'cim:ExcAC3A.ks'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcAC3A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcAC3A.seve2'})
    ta: PU = field(metadata={'xpath': 'cim:ExcAC3A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAC3A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcAC3A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAC3A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcAC3A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcAC3A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcAC3A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcAC3A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcAC3A.ve2'})
    vemin: PU = field(metadata={'xpath': 'cim:ExcAC3A.vemin'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcAC3A.vfemax'})
    vlv: PU = field(metadata={'xpath': 'cim:ExcAC3A.vlv'})
