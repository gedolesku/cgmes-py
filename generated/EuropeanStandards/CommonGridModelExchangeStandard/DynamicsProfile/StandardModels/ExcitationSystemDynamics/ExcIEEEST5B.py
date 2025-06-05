from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST5B(ExcitationSystemDynamics):
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEST5B.kc'})
    kr: PU = field(metadata={'xpath': 'cim:ExcIEEEST5B.kr'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.t1'})
    tb1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tb1'})
    tb2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tb2'})
    tc1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tc1'})
    tc2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tc2'})
    tob1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tob1'})
    tob2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tob2'})
    toc1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.toc1'})
    toc2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.toc2'})
    tub1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tub1'})
    tub2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tub2'})
    tuc1: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tuc1'})
    tuc2: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST5B.tuc2'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST5B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST5B.vrmin'})
