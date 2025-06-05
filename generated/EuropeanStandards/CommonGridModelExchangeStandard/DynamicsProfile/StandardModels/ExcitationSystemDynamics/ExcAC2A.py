from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAC2A(ExcitationSystemDynamics):
    hvgate: Boolean = field(metadata={'xpath': 'cim:ExcAC2A.hvgate'})
    ka: PU = field(metadata={'xpath': 'cim:ExcAC2A.ka'})
    kb: PU = field(metadata={'xpath': 'cim:ExcAC2A.kb'})
    kb1: PU = field(metadata={'xpath': 'cim:ExcAC2A.kb1'})
    kc: PU = field(metadata={'xpath': 'cim:ExcAC2A.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcAC2A.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcAC2A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcAC2A.kf'})
    kh: PU = field(metadata={'xpath': 'cim:ExcAC2A.kh'})
    kl: PU = field(metadata={'xpath': 'cim:ExcAC2A.kl'})
    kl1: PU = field(metadata={'xpath': 'cim:ExcAC2A.kl1'})
    ks: PU = field(metadata={'xpath': 'cim:ExcAC2A.ks'})
    lvgate: Boolean = field(metadata={'xpath': 'cim:ExcAC2A.lvgate'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcAC2A.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcAC2A.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAC2A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAC2A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcAC2A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAC2A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcAC2A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcAC2A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcAC2A.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcAC2A.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcAC2A.ve2'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcAC2A.vfemax'})
    vlr: PU = field(metadata={'xpath': 'cim:ExcAC2A.vlr'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcAC2A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcAC2A.vrmin'})
