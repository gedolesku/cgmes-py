from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcDC3A(ExcitationSystemDynamics):
    edfmax: PU = field(metadata={'xpath': 'cim:ExcDC3A.edfmax'})
    efd1: PU = field(metadata={'xpath': 'cim:ExcDC3A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcDC3A.efd2'})
    efdlim: Boolean = field(metadata={'xpath': 'cim:ExcDC3A.efdlim'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcDC3A.efdmin'})
    exclim: Boolean = field(metadata={'xpath': 'cim:ExcDC3A.exclim'})
    ke: PU = field(metadata={'xpath': 'cim:ExcDC3A.ke'})
    kr: PU = field(metadata={'xpath': 'cim:ExcDC3A.kr'})
    ks: PU = field(metadata={'xpath': 'cim:ExcDC3A.ks'})
    kv: PU = field(metadata={'xpath': 'cim:ExcDC3A.kv'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcDC3A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcDC3A.seefd2'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcDC3A.te'})
    trh: Seconds = field(metadata={'xpath': 'cim:ExcDC3A.trh'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcDC3A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcDC3A.vrmin'})
