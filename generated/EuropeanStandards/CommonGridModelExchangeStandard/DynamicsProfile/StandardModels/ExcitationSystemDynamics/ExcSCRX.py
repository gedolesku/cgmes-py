from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcSCRX(ExcitationSystemDynamics):
    cswitch: Boolean = field(metadata={'xpath': 'cim:ExcSCRX.cswitch'})
    emax: PU = field(metadata={'xpath': 'cim:ExcSCRX.emax'})
    emin: PU = field(metadata={'xpath': 'cim:ExcSCRX.emin'})
    k: PU = field(metadata={'xpath': 'cim:ExcSCRX.k'})
    rcrfd: Simple_Float = field(metadata={'xpath': 'cim:ExcSCRX.rcrfd'})
    tatb: Simple_Float = field(metadata={'xpath': 'cim:ExcSCRX.tatb'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcSCRX.tb'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcSCRX.te'})
