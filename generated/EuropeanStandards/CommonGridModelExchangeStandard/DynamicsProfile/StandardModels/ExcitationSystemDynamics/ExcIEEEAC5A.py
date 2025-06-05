from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC5A(ExcitationSystemDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.efd2'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.kf'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC5A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEAC5A.seefd2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC5A.ta'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC5A.te'})
    tf1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC5A.tf1'})
    tf2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC5A.tf2'})
    tf3: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC5A.tf3'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC5A.vrmin'})
