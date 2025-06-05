from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC2A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.ka'})
    kb: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.kb'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.kf'})
    kh: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.kh'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC2A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC2A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC2A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC2A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC2A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC2A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC2A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.ve2'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.vfemax'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC2A.vrmin'})
