from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcHU(ExcitationSystemDynamics):
    ae: PU = field(metadata={'xpath': 'cim:ExcHU.ae'})
    ai: PU = field(metadata={'xpath': 'cim:ExcHU.ai'})
    atr: PU = field(metadata={'xpath': 'cim:ExcHU.atr'})
    emax: PU = field(metadata={'xpath': 'cim:ExcHU.emax'})
    emin: PU = field(metadata={'xpath': 'cim:ExcHU.emin'})
    imax: PU = field(metadata={'xpath': 'cim:ExcHU.imax'})
    imin: PU = field(metadata={'xpath': 'cim:ExcHU.imin'})
    ke: Simple_Float = field(metadata={'xpath': 'cim:ExcHU.ke'})
    ki: Simple_Float = field(metadata={'xpath': 'cim:ExcHU.ki'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcHU.te'})
    ti: Seconds = field(metadata={'xpath': 'cim:ExcHU.ti'})
    tr: Seconds = field(metadata={'xpath': 'cim:ExcHU.tr'})
