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
class GovHydro3(TurbineGovernorDynamics):
    at: PU = field(metadata={'xpath': 'cim:GovHydro3.at'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydro3.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovHydro3.db2'})
    dturb: PU = field(metadata={'xpath': 'cim:GovHydro3.dturb'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovHydro3.eps'})
    governorControl: Boolean = field(metadata={'xpath': 'cim:GovHydro3.governorControl'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydro3.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydro3.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydro3.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovHydro3.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovHydro3.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovHydro3.gv6'})
    h0: PU = field(metadata={'xpath': 'cim:GovHydro3.h0'})
    k1: PU = field(metadata={'xpath': 'cim:GovHydro3.k1'})
    k2: PU = field(metadata={'xpath': 'cim:GovHydro3.k2'})
    kg: PU = field(metadata={'xpath': 'cim:GovHydro3.kg'})
    ki: PU = field(metadata={'xpath': 'cim:GovHydro3.ki'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydro3.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydro3.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydro3.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydro3.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovHydro3.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovHydro3.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovHydro3.pgv6'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydro3.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydro3.pmin'})
    qnl: PU = field(metadata={'xpath': 'cim:GovHydro3.qnl'})
    relec: PU = field(metadata={'xpath': 'cim:GovHydro3.relec'})
    rgate: PU = field(metadata={'xpath': 'cim:GovHydro3.rgate'})
    td: Seconds = field(metadata={'xpath': 'cim:GovHydro3.td'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovHydro3.tf'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovHydro3.tp'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovHydro3.tt'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydro3.tw'})
    velcl: Simple_Float = field(metadata={'xpath': 'cim:GovHydro3.velcl'})
    velop: Simple_Float = field(metadata={'xpath': 'cim:GovHydro3.velop'})
