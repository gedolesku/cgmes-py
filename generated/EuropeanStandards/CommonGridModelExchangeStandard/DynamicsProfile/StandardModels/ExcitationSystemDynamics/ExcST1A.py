from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcST1A(ExcitationSystemDynamics):
    ilr: PU = field(metadata={'xpath': 'cim:ExcST1A.ilr'})
    ka: PU = field(metadata={'xpath': 'cim:ExcST1A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcST1A.kc'})
    kf: PU = field(metadata={'xpath': 'cim:ExcST1A.kf'})
    klr: PU = field(metadata={'xpath': 'cim:ExcST1A.klr'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcST1A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcST1A.tb'})
    tb1: Seconds = field(metadata={'xpath': 'cim:ExcST1A.tb1'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcST1A.tc'})
    tc1: Seconds = field(metadata={'xpath': 'cim:ExcST1A.tc1'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcST1A.tf'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcST1A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcST1A.vamin'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcST1A.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcST1A.vimin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcST1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcST1A.vrmin'})
    xe: PU = field(metadata={'xpath': 'cim:ExcST1A.xe'})
