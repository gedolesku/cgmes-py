from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteamFV3(TurbineGovernorDynamics):
    k: PU = field(metadata={'xpath': 'cim:GovSteamFV3.k'})
    k1: PU = field(metadata={'xpath': 'cim:GovSteamFV3.k1'})
    k2: PU = field(metadata={'xpath': 'cim:GovSteamFV3.k2'})
    k3: PU = field(metadata={'xpath': 'cim:GovSteamFV3.k3'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteamFV3.mwbase'})
    pmax: PU = field(metadata={'xpath': 'cim:GovSteamFV3.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovSteamFV3.pmin'})
    prmax: PU = field(metadata={'xpath': 'cim:GovSteamFV3.prmax'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.t6'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:GovSteamFV3.tc'})
    uc: Simple_Float = field(metadata={'xpath': 'cim:GovSteamFV3.uc'})
    uo: Simple_Float = field(metadata={'xpath': 'cim:GovSteamFV3.uo'})
