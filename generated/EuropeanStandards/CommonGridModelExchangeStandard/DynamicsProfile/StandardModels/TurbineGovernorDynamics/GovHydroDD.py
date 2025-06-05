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
class GovHydroDD(TurbineGovernorDynamics):
    aturb: PU = field(metadata={'xpath': 'cim:GovHydroDD.aturb'})
    bturb: PU = field(metadata={'xpath': 'cim:GovHydroDD.bturb'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydroDD.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovHydroDD.db2'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovHydroDD.eps'})
    gmax: PU = field(metadata={'xpath': 'cim:GovHydroDD.gmax'})
    gmin: PU = field(metadata={'xpath': 'cim:GovHydroDD.gmin'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydroDD.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydroDD.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydroDD.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovHydroDD.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovHydroDD.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovHydroDD.gv6'})
    inputSignal: Boolean = field(metadata={'xpath': 'cim:GovHydroDD.inputSignal'})
    k1: PU = field(metadata={'xpath': 'cim:GovHydroDD.k1'})
    k2: PU = field(metadata={'xpath': 'cim:GovHydroDD.k2'})
    kg: PU = field(metadata={'xpath': 'cim:GovHydroDD.kg'})
    ki: PU = field(metadata={'xpath': 'cim:GovHydroDD.ki'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydroDD.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydroDD.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydroDD.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydroDD.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovHydroDD.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovHydroDD.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovHydroDD.pgv6'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydroDD.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydroDD.pmin'})
    r: PU = field(metadata={'xpath': 'cim:GovHydroDD.r'})
    td: Seconds = field(metadata={'xpath': 'cim:GovHydroDD.td'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovHydroDD.tf'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovHydroDD.tp'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovHydroDD.tt'})
    tturb: Seconds = field(metadata={'xpath': 'cim:GovHydroDD.tturb'})
    velcl: Simple_Float = field(metadata={'xpath': 'cim:GovHydroDD.velcl'})
    velop: Simple_Float = field(metadata={'xpath': 'cim:GovHydroDD.velop'})
