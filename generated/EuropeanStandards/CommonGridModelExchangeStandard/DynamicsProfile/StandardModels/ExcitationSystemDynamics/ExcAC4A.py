from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAC4A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcAC4A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcAC4A.kc'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAC4A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAC4A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcAC4A.tc'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcAC4A.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcAC4A.vimin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcAC4A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcAC4A.vrmin'})
