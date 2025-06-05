from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Frequency import Frequency
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydro4(TurbineGovernorDynamics):
    at: PU = field(metadata={'xpath': 'cim:GovHydro4.at'})
    bgv0: PU = field(metadata={'xpath': 'cim:GovHydro4.bgv0'})
    bgv1: PU = field(metadata={'xpath': 'cim:GovHydro4.bgv1'})
    bgv2: PU = field(metadata={'xpath': 'cim:GovHydro4.bgv2'})
    bgv3: PU = field(metadata={'xpath': 'cim:GovHydro4.bgv3'})
    bgv4: PU = field(metadata={'xpath': 'cim:GovHydro4.bgv4'})
    bgv5: PU = field(metadata={'xpath': 'cim:GovHydro4.bgv5'})
    bmax: Simple_Float = field(metadata={'xpath': 'cim:GovHydro4.bmax'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydro4.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovHydro4.db2'})
    dturb: PU = field(metadata={'xpath': 'cim:GovHydro4.dturb'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovHydro4.eps'})
    gmax: PU = field(metadata={'xpath': 'cim:GovHydro4.gmax'})
    gmin: PU = field(metadata={'xpath': 'cim:GovHydro4.gmin'})
    gv0: PU = field(metadata={'xpath': 'cim:GovHydro4.gv0'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydro4.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydro4.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydro4.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovHydro4.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovHydro4.gv5'})
    hdam: PU = field(metadata={'xpath': 'cim:GovHydro4.hdam'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydro4.mwbase'})
    pgv0: PU = field(metadata={'xpath': 'cim:GovHydro4.pgv0'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydro4.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydro4.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydro4.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovHydro4.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovHydro4.pgv5'})
    qn1: PU = field(metadata={'xpath': 'cim:GovHydro4.qn1'})
    rperm: Seconds = field(metadata={'xpath': 'cim:GovHydro4.rperm'})
    rtemp: Seconds = field(metadata={'xpath': 'cim:GovHydro4.rtemp'})
    tblade: Seconds = field(metadata={'xpath': 'cim:GovHydro4.tblade'})
    tg: Seconds = field(metadata={'xpath': 'cim:GovHydro4.tg'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovHydro4.tp'})
    tr: Seconds = field(metadata={'xpath': 'cim:GovHydro4.tr'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydro4.tw'})
    uc: Simple_Float = field(metadata={'xpath': 'cim:GovHydro4.uc'})
    uo: Simple_Float = field(metadata={'xpath': 'cim:GovHydro4.uo'})
