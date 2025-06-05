from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcCZ(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcCZ.efdmax'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcCZ.efdmin'})
    ka: PU = field(metadata={'xpath': 'cim:ExcCZ.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcCZ.ke'})
    kp: PU = field(metadata={'xpath': 'cim:ExcCZ.kp'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcCZ.ta'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcCZ.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcCZ.te'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcCZ.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcCZ.vrmin'})
