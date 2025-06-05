from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContRotorRIEC(IdentifiedObject):
    kirr: PU = field(metadata={'xpath': 'cim:WindContRotorRIEC.kirr'})
    komegafilt: Simple_Float = field(metadata={'xpath': 'cim:WindContRotorRIEC.komegafilt'})
    kpfilt: Simple_Float = field(metadata={'xpath': 'cim:WindContRotorRIEC.kpfilt'})
    kprr: PU = field(metadata={'xpath': 'cim:WindContRotorRIEC.kprr'})
    rmax: PU = field(metadata={'xpath': 'cim:WindContRotorRIEC.rmax'})
    rmin: PU = field(metadata={'xpath': 'cim:WindContRotorRIEC.rmin'})
    tomegafilt: Seconds = field(metadata={'xpath': 'cim:WindContRotorRIEC.tomegafilt'})
    tpfilt: Seconds = field(metadata={'xpath': 'cim:WindContRotorRIEC.tpfilt'})
