from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEDC3A(ExcitationSystemDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:ExcIEEEDC3A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcIEEEDC3A.efd2'})
    exclim: Boolean = field(metadata={'xpath': 'cim:ExcIEEEDC3A.exclim'})
    ke: PU = field(metadata={'xpath': 'cim:ExcIEEEDC3A.ke'})
    kv: PU = field(metadata={'xpath': 'cim:ExcIEEEDC3A.kv'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC3A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcIEEEDC3A.seefd2'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC3A.te'})
    trh: Seconds = field(metadata={'xpath': 'cim:ExcIEEEDC3A.trh'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEDC3A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEDC3A.vrmin'})
