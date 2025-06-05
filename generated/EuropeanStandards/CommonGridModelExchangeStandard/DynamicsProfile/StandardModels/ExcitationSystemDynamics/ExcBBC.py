from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcBBC(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcBBC.efdmax'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcBBC.efdmin'})
    k: PU = field(metadata={'xpath': 'cim:ExcBBC.k'})
    switch: Boolean = field(metadata={'xpath': 'cim:ExcBBC.switch'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcBBC.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:ExcBBC.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:ExcBBC.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:ExcBBC.t4'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcBBC.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcBBC.vrmin'})
    xe: PU = field(metadata={'xpath': 'cim:ExcBBC.xe'})
