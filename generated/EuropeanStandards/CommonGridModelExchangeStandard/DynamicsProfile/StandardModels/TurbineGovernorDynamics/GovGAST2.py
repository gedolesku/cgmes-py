from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ....DomainProfile.Temperature import Temperature
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovGAST2(TurbineGovernorDynamics):
    a: Simple_Float = field(metadata={'xpath': 'cim:GovGAST2.a'})
    af1: PU = field(metadata={'xpath': 'cim:GovGAST2.af1'})
    af2: PU = field(metadata={'xpath': 'cim:GovGAST2.af2'})
    b: Simple_Float = field(metadata={'xpath': 'cim:GovGAST2.b'})
    bf1: PU = field(metadata={'xpath': 'cim:GovGAST2.bf1'})
    bf2: PU = field(metadata={'xpath': 'cim:GovGAST2.bf2'})
    c: Simple_Float = field(metadata={'xpath': 'cim:GovGAST2.c'})
    cf2: PU = field(metadata={'xpath': 'cim:GovGAST2.cf2'})
    ecr: Seconds = field(metadata={'xpath': 'cim:GovGAST2.ecr'})
    etd: Seconds = field(metadata={'xpath': 'cim:GovGAST2.etd'})
    k3: PU = field(metadata={'xpath': 'cim:GovGAST2.k3'})
    k4: PU = field(metadata={'xpath': 'cim:GovGAST2.k4'})
    k5: PU = field(metadata={'xpath': 'cim:GovGAST2.k5'})
    k6: PU = field(metadata={'xpath': 'cim:GovGAST2.k6'})
    kf: PU = field(metadata={'xpath': 'cim:GovGAST2.kf'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovGAST2.mwbase'})
    t: Seconds = field(metadata={'xpath': 'cim:GovGAST2.t'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovGAST2.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovGAST2.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovGAST2.t5'})
    tc: Temperature = field(metadata={'xpath': 'cim:GovGAST2.tc'})
    tcd: Seconds = field(metadata={'xpath': 'cim:GovGAST2.tcd'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovGAST2.tf'})
    tmax: PU = field(metadata={'xpath': 'cim:GovGAST2.tmax'})
    tmin: PU = field(metadata={'xpath': 'cim:GovGAST2.tmin'})
    tr: Temperature = field(metadata={'xpath': 'cim:GovGAST2.tr'})
    trate: ActivePower = field(metadata={'xpath': 'cim:GovGAST2.trate'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovGAST2.tt'})
    w: PU = field(metadata={'xpath': 'cim:GovGAST2.w'})
    x: Seconds = field(metadata={'xpath': 'cim:GovGAST2.x'})
    y: Seconds = field(metadata={'xpath': 'cim:GovGAST2.y'})
    z: Boolean = field(metadata={'xpath': 'cim:GovGAST2.z'})
