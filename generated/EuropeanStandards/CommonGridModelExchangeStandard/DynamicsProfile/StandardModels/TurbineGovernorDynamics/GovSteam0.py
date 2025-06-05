from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteam0(TurbineGovernorDynamics):
    dt: PU = field(metadata={'xpath': 'cim:GovSteam0.dt'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteam0.mwbase'})
    r: PU = field(metadata={'xpath': 'cim:GovSteam0.r'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteam0.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovSteam0.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovSteam0.t3'})
    vmax: PU = field(metadata={'xpath': 'cim:GovSteam0.vmax'})
    vmin: PU = field(metadata={'xpath': 'cim:GovSteam0.vmin'})
