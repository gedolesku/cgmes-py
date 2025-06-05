from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Simple_Float import Simple_Float
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArType2IEEEPFController(PFVArControllerType2Dynamics):
    exlon: Boolean = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.exlon'})
    ki: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.ki'})
    kp: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.kp'})
    pfref: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.pfref'})
    vclmt: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.vclmt'})
    vref: PU = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.vref'})
    vs: Simple_Float = field(metadata={'xpath': 'cim:PFVArType2IEEEPFController.vs'})
