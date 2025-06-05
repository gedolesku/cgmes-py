from __future__ import annotations
from ....DomainProfile.AngleDegrees import AngleDegrees
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST4B(ExcitationSystemDynamics):
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kc'})
    kg: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kg'})
    ki: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.ki'})
    kim: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kim'})
    kir: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kir'})
    kp: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kp'})
    kpm: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kpm'})
    kpr: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.kpr'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST4B.ta'})
    thetap: AngleDegrees = field(metadata={'xpath': 'cim:ExcIEEEST4B.thetap'})
    vbmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.vbmax'})
    vmmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.vmmax'})
    vmmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.vmmin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.vrmin'})
    xl: PU = field(metadata={'xpath': 'cim:ExcIEEEST4B.xl'})
