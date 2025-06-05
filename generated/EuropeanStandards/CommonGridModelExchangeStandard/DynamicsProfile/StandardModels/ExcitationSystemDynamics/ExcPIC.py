from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcPIC(ExcitationSystemDynamics):
    e1: PU = field(metadata={'xpath': 'cim:ExcPIC.e1'})
    e2: PU = field(metadata={'xpath': 'cim:ExcPIC.e2'})
    efdmax: PU = field(metadata={'xpath': 'cim:ExcPIC.efdmax'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcPIC.efdmin'})
    ka: PU = field(metadata={'xpath': 'cim:ExcPIC.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcPIC.kc'})
    ke: PU = field(metadata={'xpath': 'cim:ExcPIC.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcPIC.kf'})
    ki: PU = field(metadata={'xpath': 'cim:ExcPIC.ki'})
    kp: PU = field(metadata={'xpath': 'cim:ExcPIC.kp'})
    se1: PU = field(metadata={'xpath': 'cim:ExcPIC.se1'})
    se2: PU = field(metadata={'xpath': 'cim:ExcPIC.se2'})
    ta1: Seconds = field(metadata={'xpath': 'cim:ExcPIC.ta1'})
    ta2: Seconds = field(metadata={'xpath': 'cim:ExcPIC.ta2'})
    ta3: Seconds = field(metadata={'xpath': 'cim:ExcPIC.ta3'})
    ta4: Seconds = field(metadata={'xpath': 'cim:ExcPIC.ta4'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcPIC.te'})
    tf1: Seconds = field(metadata={'xpath': 'cim:ExcPIC.tf1'})
    tf2: Seconds = field(metadata={'xpath': 'cim:ExcPIC.tf2'})
    vr1: PU = field(metadata={'xpath': 'cim:ExcPIC.vr1'})
    vr2: PU = field(metadata={'xpath': 'cim:ExcPIC.vr2'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcPIC.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcPIC.vrmin'})
