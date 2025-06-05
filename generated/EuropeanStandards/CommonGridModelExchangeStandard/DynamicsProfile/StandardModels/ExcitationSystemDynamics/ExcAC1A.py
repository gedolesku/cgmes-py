from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAC1A(ExcitationSystemDynamics):
    hvlvgates: Boolean = field(metadata={'xpath': 'cim:ExcAC1A.hvlvgates'})
    ka: PU = field(metadata={'xpath': 'cim:ExcAC1A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcAC1A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcAC1A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcAC1A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcAC1A.kf'})
    kf1: PU = field(metadata={'xpath': 'cim:ExcAC1A.kf1'})
    kf2: PU = field(metadata={'xpath': 'cim:ExcAC1A.kf2'})
    ks: PU = field(metadata={'xpath': 'cim:ExcAC1A.ks'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcAC1A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcAC1A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAC1A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAC1A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcAC1A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAC1A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcAC1A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcAC1A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcAC1A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcAC1A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcAC1A.ve2'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcAC1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcAC1A.vrmin'})
