from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcST2A(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcST2A.efdmax'})
    ka: PU = field(metadata={'xpath': 'cim:ExcST2A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcST2A.kc'})
    ke: PU = field(metadata={'xpath': 'cim:ExcST2A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcST2A.kf'})
    ki: PU = field(metadata={'xpath': 'cim:ExcST2A.ki'})
    kp: PU = field(metadata={'xpath': 'cim:ExcST2A.kp'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcST2A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcST2A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcST2A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcST2A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcST2A.tf'})
    uelin: Boolean = field(metadata={'xpath': 'cim:ExcST2A.uelin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcST2A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcST2A.vrmin'})
