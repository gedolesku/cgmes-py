from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST2A(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.efdmax'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.kc'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.kf'})
    ki: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.ki'})
    kp: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.kp'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST2A.ta'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST2A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST2A.tf'})
    uelin: Boolean = field(metadata={'xpath': 'cim:ExcIEEEST2A.uelin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST2A.vrmin'})
