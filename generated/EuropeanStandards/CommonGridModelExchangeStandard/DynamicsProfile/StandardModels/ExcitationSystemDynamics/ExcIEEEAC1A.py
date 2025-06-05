from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC1A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.kf'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC1A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC1A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC1A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC1A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC1A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC1A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC1A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.ve2'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC1A.vrmin'})
