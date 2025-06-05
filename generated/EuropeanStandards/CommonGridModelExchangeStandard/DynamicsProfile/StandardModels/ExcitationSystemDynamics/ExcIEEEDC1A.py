from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEDC1A(ExcitationSystemDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.efd2'})
    exclim: Boolean = field(metadata={'xpath': 'cim:ExcIEEEDC1A.exclim'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.kf'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC1A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC1A.seefd2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC1A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC1A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC1A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC1A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC1A.tf'})
    uelin: Boolean = field(metadata={'xpath': 'cim:ExcIEEEDC1A.uelin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEDC1A.vrmin'})
