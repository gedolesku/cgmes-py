from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteamEU(TurbineGovernorDynamics):
    chc: Simple_Float = field(metadata={'xpath': 'cim:GovSteamEU.chc'})
    cho: Simple_Float = field(metadata={'xpath': 'cim:GovSteamEU.cho'})
    cic: PU = field(metadata={'xpath': 'cim:GovSteamEU.cic'})
    cio: PU = field(metadata={'xpath': 'cim:GovSteamEU.cio'})
    db1: PU = field(metadata={'xpath': 'cim:GovSteamEU.db1'})
    db2: PU = field(metadata={'xpath': 'cim:GovSteamEU.db2'})
    hhpmax: PU = field(metadata={'xpath': 'cim:GovSteamEU.hhpmax'})
    ke: PU = field(metadata={'xpath': 'cim:GovSteamEU.ke'})
    kfcor: PU = field(metadata={'xpath': 'cim:GovSteamEU.kfcor'})
    khp: PU = field(metadata={'xpath': 'cim:GovSteamEU.khp'})
    klp: PU = field(metadata={'xpath': 'cim:GovSteamEU.klp'})
    kwcor: PU = field(metadata={'xpath': 'cim:GovSteamEU.kwcor'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteamEU.mwbase'})
    pmax: PU = field(metadata={'xpath': 'cim:GovSteamEU.pmax'})
    prhmax: PU = field(metadata={'xpath': 'cim:GovSteamEU.prhmax'})
    simx: PU = field(metadata={'xpath': 'cim:GovSteamEU.simx'})
    tb: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tb'})
    tdp: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tdp'})
    ten: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.ten'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tf'})
    tfp: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tfp'})
    thp: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.thp'})
    tip: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tip'})
    tlp: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tlp'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tp'})
    trh: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.trh'})
    tvhp: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tvhp'})
    tvip: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tvip'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovSteamEU.tw'})
    wfmax: PU = field(metadata={'xpath': 'cim:GovSteamEU.wfmax'})
    wfmin: PU = field(metadata={'xpath': 'cim:GovSteamEU.wfmin'})
    wmax1: PU = field(metadata={'xpath': 'cim:GovSteamEU.wmax1'})
    wmax2: PU = field(metadata={'xpath': 'cim:GovSteamEU.wmax2'})
    wwmax: PU = field(metadata={'xpath': 'cim:GovSteamEU.wwmax'})
    wwmin: PU = field(metadata={'xpath': 'cim:GovSteamEU.wwmin'})
