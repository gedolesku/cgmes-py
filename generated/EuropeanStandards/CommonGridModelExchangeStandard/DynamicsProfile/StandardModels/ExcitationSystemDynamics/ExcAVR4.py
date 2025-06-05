from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAVR4(ExcitationSystemDynamics):
    imul: Boolean = field(metadata={'xpath': 'cim:ExcAVR4.imul'})
    ka: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR4.ka'})
    ke: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR4.ke'})
    kif: Simple_Float = field(metadata={'xpath': 'cim:ExcAVR4.kif'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcAVR4.t1'})
    t1if: Seconds = field(metadata={'xpath': 'cim:ExcAVR4.t1if'})
    t2: Seconds = field(metadata={'xpath': 'cim:ExcAVR4.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:ExcAVR4.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:ExcAVR4.t4'})
    tif: Seconds = field(metadata={'xpath': 'cim:ExcAVR4.tif'})
    vfmn: PU = field(metadata={'xpath': 'cim:ExcAVR4.vfmn'})
    vfmx: PU = field(metadata={'xpath': 'cim:ExcAVR4.vfmx'})
    vrmn: PU = field(metadata={'xpath': 'cim:ExcAVR4.vrmn'})
    vrmx: PU = field(metadata={'xpath': 'cim:ExcAVR4.vrmx'})
