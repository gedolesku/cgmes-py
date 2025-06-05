from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteamFV2(TurbineGovernorDynamics):
    dt: PU = field(metadata={'xpath': 'cim:GovSteamFV2.dt'})
    k: PU = field(metadata={'xpath': 'cim:GovSteamFV2.k'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteamFV2.mwbase'})
    r: PU = field(metadata={'xpath': 'cim:GovSteamFV2.r'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.t1'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.t3'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.tc'})
    ti: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.ti'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovSteamFV2.tt'})
    vmax: PU = field(metadata={'xpath': 'cim:GovSteamFV2.vmax'})
    vmin: PU = field(metadata={'xpath': 'cim:GovSteamFV2.vmin'})
