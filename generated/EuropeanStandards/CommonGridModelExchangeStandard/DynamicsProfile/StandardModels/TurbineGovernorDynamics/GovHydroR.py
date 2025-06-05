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
class GovHydroR(TurbineGovernorDynamics):
    at: PU = field(metadata={'xpath': 'cim:GovHydroR.at'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydroR.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovHydroR.db2'})
    dturb: PU = field(metadata={'xpath': 'cim:GovHydroR.dturb'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovHydroR.eps'})
    gmax: PU = field(metadata={'xpath': 'cim:GovHydroR.gmax'})
    gmin: PU = field(metadata={'xpath': 'cim:GovHydroR.gmin'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydroR.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydroR.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydroR.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovHydroR.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovHydroR.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovHydroR.gv6'})
    h0: PU = field(metadata={'xpath': 'cim:GovHydroR.h0'})
    inputSignal: Boolean = field(metadata={'xpath': 'cim:GovHydroR.inputSignal'})
    kg: PU = field(metadata={'xpath': 'cim:GovHydroR.kg'})
    ki: PU = field(metadata={'xpath': 'cim:GovHydroR.ki'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydroR.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydroR.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydroR.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydroR.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovHydroR.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovHydroR.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovHydroR.pgv6'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydroR.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydroR.pmin'})
    qnl: PU = field(metadata={'xpath': 'cim:GovHydroR.qnl'})
    r: PU = field(metadata={'xpath': 'cim:GovHydroR.r'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t7'})
    t8: Seconds = field(metadata={'xpath': 'cim:GovHydroR.t8'})
    td: Seconds = field(metadata={'xpath': 'cim:GovHydroR.td'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovHydroR.tp'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovHydroR.tt'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydroR.tw'})
    velcl: Simple_Float = field(metadata={'xpath': 'cim:GovHydroR.velcl'})
    velop: Simple_Float = field(metadata={'xpath': 'cim:GovHydroR.velop'})
