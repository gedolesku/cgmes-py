from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydro1(TurbineGovernorDynamics):
    at: PU = field(metadata={'xpath': 'cim:GovHydro1.at'})
    dturb: PU = field(metadata={'xpath': 'cim:GovHydro1.dturb'})
    gmax: PU = field(metadata={'xpath': 'cim:GovHydro1.gmax'})
    gmin: PU = field(metadata={'xpath': 'cim:GovHydro1.gmin'})
    hdam: PU = field(metadata={'xpath': 'cim:GovHydro1.hdam'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydro1.mwbase'})
    qnl: PU = field(metadata={'xpath': 'cim:GovHydro1.qnl'})
    rperm: PU = field(metadata={'xpath': 'cim:GovHydro1.rperm'})
    rtemp: PU = field(metadata={'xpath': 'cim:GovHydro1.rtemp'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovHydro1.tf'})
    tg: Seconds = field(metadata={'xpath': 'cim:GovHydro1.tg'})
    tr: Seconds = field(metadata={'xpath': 'cim:GovHydro1.tr'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydro1.tw'})
    velm: Simple_Float = field(metadata={'xpath': 'cim:GovHydro1.velm'})
