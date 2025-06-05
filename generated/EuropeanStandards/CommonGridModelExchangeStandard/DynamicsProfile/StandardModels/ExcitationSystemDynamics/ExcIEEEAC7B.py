from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC7B(ExcitationSystemDynamics):
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kd'})
    kdr: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kdr'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.ke'})
    kf1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kf1'})
    kf2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kf2'})
    kf3: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kf3'})
    kia: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kia'})
    kir: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kir'})
    kl: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kl'})
    kp: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kp'})
    kpa: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kpa'})
    kpr: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.kpr'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC7B.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC7B.seve2'})
    tdr: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC7B.tdr'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC7B.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC7B.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.vamin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.ve2'})
    vemin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.vemin'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.vfemax'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC7B.vrmin'})
