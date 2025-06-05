from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC8B(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.kd'})
    kdr: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.kdr'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.ke'})
    kir: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.kir'})
    kpr: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.kpr'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC8B.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC8B.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC8B.ta'})
    tdr: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC8B.tdr'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC8B.te'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.ve2'})
    vemin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.vemin'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.vfemax'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC8B.vrmin'})
