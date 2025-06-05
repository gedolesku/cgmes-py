from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAVR3(ExcitationSystemDynamics):
    e1: PU = field(metadata={'xpath': 'cim:ExcAVR3.e1'})
    e2: PU = field(metadata={'xpath': 'cim:ExcAVR3.e2'})
    ka: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR3.ka'})
    se1: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR3.se1'})
    se2: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR3.se2'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcAVR3.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:ExcAVR3.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:ExcAVR3.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:ExcAVR3.t4'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcAVR3.te'})
    vrmn: PU = field(metadata={'xpath': 'cim:ExcAVR3.vrmn'})
    vrmx: PU = field(metadata={'xpath': 'cim:ExcAVR3.vrmx'})
