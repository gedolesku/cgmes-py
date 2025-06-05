from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    tvarc: Seconds = field(metadata={'xpath': 'cim:PFVArType1IEEEVArController.tvarc'})
    vvar: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEVArController.vvar'})
    vvarcbw: Simple_Float = field(metadata={'xpath': 'cim:PFVArType1IEEEVArController.vvarcbw'})
    vvarref: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEVArController.vvarref'})
    vvtmax: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEVArController.vvtmax'})
    vvtmin: PU = field(metadata={'xpath': 'cim:PFVArType1IEEEVArController.vvtmin'})
