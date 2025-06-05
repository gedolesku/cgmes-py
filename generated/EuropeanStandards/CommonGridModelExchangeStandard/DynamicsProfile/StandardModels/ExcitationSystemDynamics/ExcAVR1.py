from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAVR1(ExcitationSystemDynamics):
    e1: PU = field(metadata={'xpath': 'cim:ExcAVR1.e1'})
    e2: PU = field(metadata={'xpath': 'cim:ExcAVR1.e2'})
    ka: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR1.ka'})
    kf: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR1.kf'})
    se1: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR1.se1'})
    se2: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR1.se2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAVR1.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAVR1.tb'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAVR1.te'})
    tf: Seconds = field(metadata={'xpath': 'cim:ExcAVR1.tf'})
    vrmn: PU = field(metadata={'xpath': 'cim:ExcAVR1.vrmn'})
    vrmx: PU = field(metadata={'xpath': 'cim:ExcAVR1.vrmx'})
