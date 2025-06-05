from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    ovex: Boolean = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.ovex'})
    tpfc: Seconds = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.tpfc'})
    vitmin: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.vitmin'})
    vpf: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.vpf'})
    vpfcbw: Simple_Float = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.vpfcbw'})
    vpfref: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.vpfref'})
    vvtmax: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.vvtmax'})
    vvtmin: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEPFController.vvtmin'})
