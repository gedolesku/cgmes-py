from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcIEEEST1AUELselectorKind import ExcIEEEST1AUELselectorKind
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST1A(ExcitationSystemDynamics):
    ilr: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.ilr'})
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.kc'})
    kf: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.kf'})
    klr: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.klr'})
    pssin: Boolean = field(metadata={'xpath': 'cim:ExcIEEEST1A.pssin'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST1A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST1A.tb'})
    tb1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST1A.tb1'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST1A.tc'})
    tc1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST1A.tc1'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST1A.tf'})
    uelin: ExcIEEEST1AUELselectorKind = field(metadata={'xpath': 'cim:ExcIEEEST1A.uelin'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.vamin'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.vimin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST1A.vrmin'})
