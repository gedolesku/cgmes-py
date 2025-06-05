from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Simple_Float import Simple_Float
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArType2IEEEVArController(PFVArControllerType2Dynamics):
    exlon: Boolean = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.exlon'})
    ki: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.ki'})
    kp: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.kp'})
    qref: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.qref'})
    vclmt: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.vclmt'})
    vref: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.vref'})
    vs: Simple_Float = field(metadata={'xpath': 'cim:PFVArType2IEEEVArController.vs'})
