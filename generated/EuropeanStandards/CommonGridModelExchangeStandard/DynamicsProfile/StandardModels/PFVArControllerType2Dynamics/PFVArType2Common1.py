from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArType2Common1(PFVArControllerType2Dynamics):
    j: Boolean = field(metadata={'xpath': 'cim:PFVArType2Common1.j'})
    ki: PU = field(metadata={'xpath': 'cim:PFVArType2Common1.ki'})
    kp: PU = field(metadata={'xpath': 'cim:PFVArType2Common1.kp'})
    max: PU = field(metadata={'xpath': 'cim:PFVArType2Common1.max'})
    ref: PU = field(metadata={'xpath': 'cim:PFVArType2Common1.ref'})
