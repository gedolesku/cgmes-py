from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Frequency import Frequency
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydro2(TurbineGovernorDynamics):
    aturb: PU = field(metadata={'xpath': 'cim:GovHydro2.aturb'})
    bturb: PU = field(metadata={'xpath': 'cim:GovHydro2.bturb'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydro2.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovHydro2.db2'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovHydro2.eps'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydro2.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydro2.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydro2.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovHydro2.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovHydro2.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovHydro2.gv6'})
    kturb: PU = field(metadata={'xpath': 'cim:GovHydro2.kturb'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydro2.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydro2.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydro2.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydro2.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovHydro2.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovHydro2.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovHydro2.pgv6'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydro2.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydro2.pmin'})
    rperm: PU = field(metadata={'xpath': 'cim:GovHydro2.rperm'})
    rtemp: PU = field(metadata={'xpath': 'cim:GovHydro2.rtemp'})
    tg: Seconds = field(metadata={'xpath': 'cim:GovHydro2.tg'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovHydro2.tp'})
    tr: Seconds = field(metadata={'xpath': 'cim:GovHydro2.tr'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydro2.tw'})
    uc: Simple_Float = field(metadata={'xpath': 'cim:GovHydro2.uc'})
    uo: Simple_Float = field(metadata={'xpath': 'cim:GovHydro2.uo'})
