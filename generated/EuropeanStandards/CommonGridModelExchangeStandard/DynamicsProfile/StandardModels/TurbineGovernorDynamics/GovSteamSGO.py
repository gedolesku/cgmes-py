from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteamSGO(TurbineGovernorDynamics):
    k1: PU = field(metadata={'xpath': 'cim:GovSteamSGO.k1'})
    k2: PU = field(metadata={'xpath': 'cim:GovSteamSGO.k2'})
    k3: PU = field(metadata={'xpath': 'cim:GovSteamSGO.k3'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteamSGO.mwbase'})
    pmax: PU = field(metadata={'xpath': 'cim:GovSteamSGO.pmax'})
    pmin: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.pmin'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:GovSteamSGO.t6'})
