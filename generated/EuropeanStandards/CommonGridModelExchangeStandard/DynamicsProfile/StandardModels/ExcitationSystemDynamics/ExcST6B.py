from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcST6BOELselectorKind import ExcST6BOELselectorKind
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcST6B(ExcitationSystemDynamics):
    ilr: PU = field(metadata={'xpath': 'cim:ExcST6B.ilr'})
    k1: Boolean = field(metadata={'xpath': 'cim:ExcST6B.k1'})
    kcl: PU = field(metadata={'xpath': 'cim:ExcST6B.kcl'})
    kff: PU = field(metadata={'xpath': 'cim:ExcST6B.kff'})
    kg: PU = field(metadata={'xpath': 'cim:ExcST6B.kg'})
    kia: PU = field(metadata={'xpath': 'cim:ExcST6B.kia'})
    klr: PU = field(metadata={'xpath': 'cim:ExcST6B.klr'})
    km: PU = field(metadata={'xpath': 'cim:ExcST6B.km'})
    kpa: PU = field(metadata={'xpath': 'cim:ExcST6B.kpa'})
    kvd: PU = field(metadata={'xpath': 'cim:ExcST6B.kvd'})
    oelin: ExcST6BOELselectorKind = field(metadata={'xpath': 'cim:ExcST6B.oelin'})
    tg: Seconds = field(metadata={'xpath': 'cim:ExcST6B.tg'})
    ts: Seconds = field(metadata={'xpath': 'cim:ExcST6B.ts'})
    tvd: Seconds = field(metadata={'xpath': 'cim:ExcST6B.tvd'})
    vamax: PU = field(metadata={'xpath': 'cim:ExcST6B.vamax'})
    vamin: PU = field(metadata={'xpath': 'cim:ExcST6B.vamin'})
    vilim: Boolean = field(metadata={'xpath': 'cim:ExcST6B.vilim'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcST6B.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcST6B.vimin'})
    vmult: Boolean = field(metadata={'xpath': 'cim:ExcST6B.vmult'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcST6B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcST6B.vrmin'})
    xc: PU = field(metadata={'xpath': 'cim:ExcST6B.xc'})
