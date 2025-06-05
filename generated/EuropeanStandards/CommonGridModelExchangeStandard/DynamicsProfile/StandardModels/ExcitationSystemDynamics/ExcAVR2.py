from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAVR2(ExcitationSystemDynamics):
    e1: PU = field(metadata={'xpath': 'cim:ExcAVR2.e1'})
    e2: PU = field(metadata={'xpath': 'cim:ExcAVR2.e2'})
    ka: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR2.ka'})
    kf: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR2.kf'})
    se1: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR2.se1'})
    se2: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR2.se2'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAVR2.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcAVR2.tb'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAVR2.te'})
    tf1: Seconds = field(metadata={'xpath': 'cim:ExcAVR2.tf1'})
    tf2: Seconds = field(metadata={'xpath': 'cim:ExcAVR2.tf2'})
    vrmn: PU = field(metadata={'xpath': 'cim:ExcAVR2.vrmn'})
    vrmx: PU = field(metadata={'xpath': 'cim:ExcAVR2.vrmx'})
