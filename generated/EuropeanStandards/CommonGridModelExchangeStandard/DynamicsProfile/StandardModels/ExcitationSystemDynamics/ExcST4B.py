from __future__ import annotations
from ....DomainProfile.AngleDegrees import AngleDegrees
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcST4B(ExcitationSystemDynamics):
    kc: PU = field(metadata={'xpath': 'cim:ExcST4B.kc'})
    kg: PU = field(metadata={'xpath': 'cim:ExcST4B.kg'})
    ki: PU = field(metadata={'xpath': 'cim:ExcST4B.ki'})
    kim: PU = field(metadata={'xpath': 'cim:ExcST4B.kim'})
    kir: PU = field(metadata={'xpath': 'cim:ExcST4B.kir'})
    kp: PU = field(metadata={'xpath': 'cim:ExcST4B.kp'})
    kpm: PU = field(metadata={'xpath': 'cim:ExcST4B.kpm'})
    kpr: PU = field(metadata={'xpath': 'cim:ExcST4B.kpr'})
    lvgate: Boolean = field(metadata={'xpath': 'cim:ExcST4B.lvgate'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcST4B.ta'})
    thetap: AngleDegrees = field(metadata={'xpath': 'cim:ExcST4B.thetap'})
    uel: Boolean = field(metadata={'xpath': 'cim:ExcST4B.uel'})
    vbmax: PU = field(metadata={'xpath': 'cim:ExcST4B.vbmax'})
    vgmax: PU = field(metadata={'xpath': 'cim:ExcST4B.vgmax'})
    vmmax: PU = field(metadata={'xpath': 'cim:ExcST4B.vmmax'})
    vmmin: PU = field(metadata={'xpath': 'cim:ExcST4B.vmmin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcST4B.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcST4B.vrmin'})
    xl: PU = field(metadata={'xpath': 'cim:ExcST4B.xl'})
