from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcSEXS(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcSEXS.efdmax'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcSEXS.efdmin'})
    emax: PU = field(metadata={'xpath': 'cim:ExcSEXS.emax'})
    emin: PU = field(metadata={'xpath': 'cim:ExcSEXS.emin'})
    k: PU = field(metadata={'xpath': 'cim:ExcSEXS.k'})
    kc: PU = field(metadata={'xpath': 'cim:ExcSEXS.kc'})
    tatb: Simple_Float = field(metadata={'xpath': 'cim:ExcSEXS.tatb'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcSEXS.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcSEXS.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcSEXS.te'})
