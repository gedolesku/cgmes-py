from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC3A(ExcitationSystemDynamics):
    efdn: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.efdn'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.kf'})
    kn: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.kn'})
    kr: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.kr'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC3A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC3A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC3A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC3A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC3A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC3A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC3A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.ve2'})
    vemin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.vemin'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC3A.vfemax'})
