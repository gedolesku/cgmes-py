from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovGAST(TurbineGovernorDynamics):
    at: PU = field(metadata={'xpath': 'cim:GovGAST.at'})
    dturb: PU = field(metadata={'xpath': 'cim:GovGAST.dturb'})
    kt: PU = field(metadata={'xpath': 'cim:GovGAST.kt'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovGAST.mwbase'})
    r: PU = field(metadata={'xpath': 'cim:GovGAST.r'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovGAST.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovGAST.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovGAST.t3'})
    vmax: PU = field(metadata={'xpath': 'cim:GovGAST.vmax'})
    vmin: PU = field(metadata={'xpath': 'cim:GovGAST.vmin'})
