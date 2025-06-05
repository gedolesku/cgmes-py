from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEDC4B(ExcitationSystemDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.efd2'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.ka'})
    kd: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.kf'})
    ki: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.ki'})
    kp: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.kp'})
    oelin: Boolean = field(metadata={'xpath': 'cim:ExcIEEEDC4B.oelin'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC4B.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC4B.seefd2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC4B.ta'})
    td: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC4B.td'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC4B.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC4B.tf'})
    uelin: Boolean = field(metadata={'xpath': 'cim:ExcIEEEDC4B.uelin'})
    vemin: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.vemin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEDC4B.vrmin'})
