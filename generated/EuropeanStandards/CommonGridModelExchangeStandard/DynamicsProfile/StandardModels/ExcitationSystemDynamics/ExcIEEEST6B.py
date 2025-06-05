from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcST6BOELselectorKind import ExcST6BOELselectorKind
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST6B(ExcitationSystemDynamics):
    ilr: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.ilr'})
    kci: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.kci'})
    kff: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.kff'})
    kg: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.kg'})
    kia: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.kia'})
    klr: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.klr'})
    km: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.km'})
    kpa: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.kpa'})
    oelin: ExcST6BOELselectorKind = field(metadata={'xpath': 'cim:ExcIEEEST6B.oelin'})
    tg: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST6B.tg'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.vamin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST6B.vrmin'})
