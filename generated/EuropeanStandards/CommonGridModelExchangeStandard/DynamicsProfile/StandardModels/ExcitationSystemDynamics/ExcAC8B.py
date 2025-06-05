from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAC8B(ExcitationSystemDynamics):
    inlim: Boolean = field(metadata={'xpath': 'cim:ExcAC8B.inlim'})
    ka: PU = field(metadata={'xpath': 'cim:ExcAC8B.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcAC8B.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcAC8B.kd'})
    kdr: PU = field(metadata={'xpath': 'cim:ExcAC8B.kdr'})
    ke: PU = field(metadata={'xpath': 'cim:ExcAC8B.ke'})
    kir: PU = field(metadata={'xpath': 'cim:ExcAC8B.kir'})
    kpr: PU = field(metadata={'xpath': 'cim:ExcAC8B.kpr'})
    ks: PU = field(metadata={'xpath': 'cim:ExcAC8B.ks'})
    pidlim: Boolean = field(metadata={'xpath': 'cim:ExcAC8B.pidlim'})
    seve1: Simple_Float = field(metadata={'xpath': 'cim:ExcAC8B.seve1'})
    seve2: Simple_Float = field(metadata={'xpath': 'cim:ExcAC8B.seve2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAC8B.ta'})
    tdr: Seconds = field(metadata={'xpath': 'cim:ExcAC8B.tdr'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAC8B.te'})
    telim: Boolean = field(metadata={'xpath': 'cim:ExcAC8B.telim'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcAC8B.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcAC8B.ve2'})
    vemin: PU = field(metadata={'xpath': 'cim:ExcAC8B.vemin'})
    vfemax: PU = field(metadata={'xpath': 'cim:ExcAC8B.vfemax'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcAC8B.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcAC8B.vimin'})
    vpidmax: PU = field(metadata={'xpath': 'cim:ExcAC8B.vpidmax'})
    vpidmin: PU = field(metadata={'xpath': 'cim:ExcAC8B.vpidmin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcAC8B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcAC8B.vrmin'})
    vtmult: Boolean = field(metadata={'xpath': 'cim:ExcAC8B.vtmult'})
