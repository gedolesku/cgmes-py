from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcDC1A(ExcitationSystemDynamics):
    edfmax: PU = field(metadata={'xpath': 'cim:ExcDC1A.edfmax'})
    efd1: PU = field(metadata={'xpath': 'cim:ExcDC1A.efd1'})
    efd2: PU = field(metadata={'xpath': 'cim:ExcDC1A.efd2'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcDC1A.efdmin'})
    exclim: Boolean = field(metadata={'xpath': 'cim:ExcDC1A.exclim'})
    ka: PU = field(metadata={'xpath': 'cim:ExcDC1A.ka'})
    ke: PU = field(metadata={'xpath': 'cim:ExcDC1A.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcDC1A.kf'})
    ks: PU = field(metadata={'xpath': 'cim:ExcDC1A.ks'})
    seefd1: Simple_Float = field(metadata={'xpath': 'cim:ExcDC1A.seefd1'})
    seefd2: Simple_Float = field(metadata={'xpath': 'cim:ExcDC1A.seefd2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcDC1A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcDC1A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcDC1A.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcDC1A.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcDC1A.tf'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcDC1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcDC1A.vrmin'})
