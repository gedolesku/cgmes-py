from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEAC4A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEAC4A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEAC4A.kc'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC4A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC4A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEAC4A.tc'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC4A.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC4A.vimin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEAC4A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEAC4A.vrmin'})
