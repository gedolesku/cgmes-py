from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcST7BOELselectorKind import ExcST7BOELselectorKind
from .ExcST7BUELselectorKind import ExcST7BUELselectorKind
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST7B(ExcitationSystemDynamics):
    kh: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.kh'})
    kia: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.kia'})
    kl: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.kl'})
    kpa: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.kpa'})
    oelin: ExcST7BOELselectorKind = field(metadata={'xpath': 'cim:ExcIEEEST7B.oelin'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST7B.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST7B.tc'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST7B.tf'})
    tg: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST7B.tg'})
    tia: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST7B.tia'})
    uelin: ExcST7BUELselectorKind = field(metadata={'xpath': 'cim:ExcIEEEST7B.uelin'})
    vmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.vmax'})
    vmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.vmin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST7B.vrmin'})
