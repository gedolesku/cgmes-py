from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAVR7(ExcitationSystemDynamics):
    a1: PU = field(metadata={'xpath': 'cim:ExcAVR7.a1'})
    a2: PU = field(metadata={'xpath': 'cim:ExcAVR7.a2'})
    a3: PU = field(metadata={'xpath': 'cim:ExcAVR7.a3'})
    a4: PU = field(metadata={'xpath': 'cim:ExcAVR7.a4'})
    a5: PU = field(metadata={'xpath': 'cim:ExcAVR7.a5'})
    a6: PU = field(metadata={'xpath': 'cim:ExcAVR7.a6'})
    k1: PU = field(metadata={'xpath': 'cim:ExcAVR7.k1'})
    k3: PU = field(metadata={'xpath': 'cim:ExcAVR7.k3'})
    k5: PU = field(metadata={'xpath': 'cim:ExcAVR7.k5'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcAVR7.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:ExcAVR7.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:ExcAVR7.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:ExcAVR7.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:ExcAVR7.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:ExcAVR7.t6'})
    vmax1: PU = field(metadata={'xpath': 'cim:ExcAVR7.vmax1'})
    vmax3: PU = field(metadata={'xpath': 'cim:ExcAVR7.vmax3'})
    vmax5: PU = field(metadata={'xpath': 'cim:ExcAVR7.vmax5'})
    vmin1: PU = field(metadata={'xpath': 'cim:ExcAVR7.vmin1'})
    vmin3: PU = field(metadata={'xpath': 'cim:ExcAVR7.vmin3'})
    vmin5: PU = field(metadata={'xpath': 'cim:ExcAVR7.vmin5'})
