from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcDC3A1(ExcitationSystemDynamics):
    exclim: Boolean = field(metadata={'xpath': 'cim:ExcDC3A1.exclim'})
    ka: PU = field(metadata={'xpath': 'cim:ExcDC3A1.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcDC3A1.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcDC3A1.kf'})
    ki: PU = field(metadata={'xpath': 'cim:ExcDC3A1.ki'})
    kp: PU = field(metadata={'xpath': 'cim:ExcDC3A1.kp'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcDC3A1.ta'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcDC3A1.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcDC3A1.tf'})
    vb1max: PU = field(metadata={'xpath': 'cim:ExcDC3A1.vb1max'})
    vblim: Boolean = field(metadata={'xpath': 'cim:ExcDC3A1.vblim'})
    vbmax: PU = field(metadata={'xpath': 'cim:ExcDC3A1.vbmax'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcDC3A1.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcDC3A1.vrmin'})
