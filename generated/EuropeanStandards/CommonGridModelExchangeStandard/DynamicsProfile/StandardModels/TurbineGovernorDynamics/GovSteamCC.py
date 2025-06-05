from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteamCC(TurbineGovernorDynamics):
    dhp: PU = field(metadata={'xpath': 'cim:GovSteamCC.dhp'})
    dlp: PU = field(metadata={'xpath': 'cim:GovSteamCC.dlp'})
    fhp: PU = field(metadata={'xpath': 'cim:GovSteamCC.fhp'})
    flp: PU = field(metadata={'xpath': 'cim:GovSteamCC.flp'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteamCC.mwbase'})
    pmaxhp: PU = field(metadata={'xpath': 'cim:GovSteamCC.pmaxhp'})
    pmaxlp: PU = field(metadata={'xpath': 'cim:GovSteamCC.pmaxlp'})
    rhp: PU = field(metadata={'xpath': 'cim:GovSteamCC.rhp'})
    rlp: PU = field(metadata={'xpath': 'cim:GovSteamCC.rlp'})
    t1hp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t1hp'})
    t1lp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t1lp'})
    t3hp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t3hp'})
    t3lp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t3lp'})
    t4hp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t4hp'})
    t4lp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t4lp'})
    t5hp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t5hp'})
    t5lp: Seconds = field(metadata={'xpath': 'cim:GovSteamCC.t5lp'})
