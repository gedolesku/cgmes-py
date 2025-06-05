from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcOEX3T(ExcitationSystemDynamics):
    e1: PU = field(metadata={'xpath': 'cim:ExcOEX3T.e1'})
    e2: PU = field(metadata={'xpath': 'cim:ExcOEX3T.e2'})
    ka: PU = field(metadata={'xpath': 'cim:ExcOEX3T.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcOEX3T.kc'})
    kd: PU = field(metadata={'xpath': 'cim:ExcOEX3T.kd'})
    ke: PU = field(metadata={'xpath': 'cim:ExcOEX3T.ke'})
    kf: PU = field(metadata={'xpath': 'cim:ExcOEX3T.kf'})
    see1: PU = field(metadata={'xpath': 'cim:ExcOEX3T.see1'})
    see2: PU = field(metadata={'xpath': 'cim:ExcOEX3T.see2'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.t6'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcOEX3T.tf'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcOEX3T.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcOEX3T.vrmin'})
