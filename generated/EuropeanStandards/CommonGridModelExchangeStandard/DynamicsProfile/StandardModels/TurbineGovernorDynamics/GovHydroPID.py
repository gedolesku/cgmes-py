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
class GovHydroPID(TurbineGovernorDynamics):
    aturb: PU = field(metadata={'xpath': 'cim:GovHydroPID.aturb'})
    bturb: PU = field(metadata={'xpath': 'cim:GovHydroPID.bturb'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydroPID.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovHydroPID.db2'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovHydroPID.eps'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydroPID.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydroPID.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydroPID.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovHydroPID.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovHydroPID.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovHydroPID.gv6'})
    inputSignal: Boolean = field(metadata={'xpath': 'cim:GovHydroPID.inputSignal'})
    kd: PU = field(metadata={'xpath': 'cim:GovHydroPID.kd'})
    kg: PU = field(metadata={'xpath': 'cim:GovHydroPID.kg'})
    ki: PU = field(metadata={'xpath': 'cim:GovHydroPID.ki'})
    kp: PU = field(metadata={'xpath': 'cim:GovHydroPID.kp'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydroPID.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydroPID.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydroPID.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydroPID.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovHydroPID.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovHydroPID.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovHydroPID.pgv6'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydroPID.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydroPID.pmin'})
    r: PU = field(metadata={'xpath': 'cim:GovHydroPID.r'})
    td: Seconds = field(metadata={'xpath': 'cim:GovHydroPID.td'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovHydroPID.tf'})
    tp: Seconds = field(metadata={'xpath': 'cim:GovHydroPID.tp'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovHydroPID.tt'})
    tturb: Seconds = field(metadata={'xpath': 'cim:GovHydroPID.tturb'})
    velcl: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPID.velcl'})
    velop: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPID.velop'})
