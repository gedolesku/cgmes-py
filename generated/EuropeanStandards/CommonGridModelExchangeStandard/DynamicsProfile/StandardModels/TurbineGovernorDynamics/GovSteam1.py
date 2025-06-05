from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.Frequency import Frequency
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovSteam1(TurbineGovernorDynamics):
    db1: Frequency = field(metadata={'xpath': 'cim:GovSteam1.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovSteam1.db2'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovSteam1.eps'})
    gv1: PU = field(metadata={'xpath': 'cim:GovSteam1.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovSteam1.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovSteam1.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovSteam1.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovSteam1.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovSteam1.gv6'})
    k: PU = field(metadata={'xpath': 'cim:GovSteam1.k'})
    k1: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k1'})
    k2: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k2'})
    k3: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k3'})
    k4: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k4'})
    k5: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k5'})
    k6: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k6'})
    k7: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k7'})
    k8: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.k8'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovSteam1.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovSteam1.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovSteam1.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovSteam1.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovSteam1.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovSteam1.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovSteam1.pgv6'})
    pmax: PU = field(metadata={'xpath': 'cim:GovSteam1.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovSteam1.pmin'})
    sdb1: Boolean = field(metadata={'xpath': 'cim:GovSteam1.sdb1'})
    sdb2: Boolean = field(metadata={'xpath': 'cim:GovSteam1.sdb2'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:GovSteam1.t7'})
    uc: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.uc'})
    uo: Simple_Float = field(metadata={'xpath': 'cim:GovSteam1.uo'})
    valve: Boolean = field(metadata={'xpath': 'cim:GovSteam1.valve'})
