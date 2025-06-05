from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteamIEEE1(TurbineGovernorDynamics):
    k: PU = field(metadata={'xpath': 'cim:GovSteamIEEE1.k'})
    k1: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k1'})
    k2: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k2'})
    k3: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k3'})
    k4: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k4'})
    k5: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k5'})
    k6: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k6'})
    k7: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k7'})
    k8: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.k8'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteamIEEE1.mwbase'})
    pmax: PU = field(metadata={'xpath': 'cim:GovSteamIEEE1.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovSteamIEEE1.pmin'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:GovSteamIEEE1.t7'})
    uc: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.uc'})
    uo: Simple_Float = field(metadata={'xpath': 'cim:GovSteamIEEE1.uo'})
