from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteam2(TurbineGovernorDynamics):
    dbf: PU = field(metadata={'xpath': 'cim:GovSteam2.dbf'})
    k: Simple_Float = field(metadata={'xpath': 'cim:GovSteam2.k'})
    mnef: PU = field(metadata={'xpath': 'cim:GovSteam2.mnef'})
    mxef: PU = field(metadata={'xpath': 'cim:GovSteam2.mxef'})
    pmax: PU = field(metadata={'xpath': 'cim:GovSteam2.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovSteam2.pmin'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteam2.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovSteam2.t2'})
