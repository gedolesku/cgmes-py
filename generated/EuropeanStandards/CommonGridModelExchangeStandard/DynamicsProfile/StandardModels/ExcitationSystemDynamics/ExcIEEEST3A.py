from __future__ import annotations
from ....DomainProfile.AngleDegrees import AngleDegrees
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcIEEEST3A(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.ka'})
    kc: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.kc'})
    kg: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.kg'})
    ki: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.ki'})
    km: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.km'})
    kp: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.kp'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST3A.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST3A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST3A.tc'})
    thetap: AngleDegrees = field(metadata={'xpath': 'cim:ExcIEEEST3A.thetap'})
    tm: Seconds = field(metadata={'xpath': 'cim:ExcIEEEST3A.tm'})
    vbmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vbmax'})
    vgmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vgmax'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vimin'})
    vmmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vmmax'})
    vmmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vmmin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.vrmin'})
    xl: PU = field(metadata={'xpath': 'cim:ExcIEEEST3A.xl'})
