from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEDC2A(ExcitationSystemDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.efd2'})
    exclim: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.exclim'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.kf'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC2A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC2A.seefd2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC2A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC2A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC2A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC2A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC2A.tf'})
    uelin: Boolean = field(metadata={'xpath': 'cim:ExcIEEEDC2A.uelin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEDC2A.vrmin'})
