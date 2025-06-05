from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcDC2A(ExcitationSystemDynamics):
    efd1: PU = field(metadata={'xpath': 'cim:ExcDC2A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcDC2A.efd2'})
    exclim: Boolean = field(metadata={'xpath': 'cim:ExcDC2A.exclim'})
    ka: PU = field(metadata={'xpath': 'cim:ExcDC2A.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcDC2A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcDC2A.kf'})
    ks: PU = field(metadata={'xpath': 'cim:ExcDC2A.ks'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcDC2A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcDC2A.seefd2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcDC2A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcDC2A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcDC2A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcDC2A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcDC2A.tf'})
    tf1: Seconds = field(metadata={'xpath': 'cim:ExcDC2A.tf1'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcDC2A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcDC2A.vrmin'})
    vtlim: Boolean = field(metadata={'xpath': 'cim:ExcDC2A.vtlim'})
