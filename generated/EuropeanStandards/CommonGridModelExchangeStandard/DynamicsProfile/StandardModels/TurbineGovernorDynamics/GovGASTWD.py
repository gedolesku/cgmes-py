from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ....DomainProfile.Temperature import Temperature
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovGASTWD(TurbineGovernorDynamics):
    a: Simple_Float = field(metadata={'xpath': 'cim:GovGASTWD.a'})
    af1: PU = field(metadata={'xpath': 'cim:GovGASTWD.af1'})
    af2: PU = field(metadata={'xpath': 'cim:GovGASTWD.af2'})
    b: Simple_Float = field(metadata={'xpath': 'cim:GovGASTWD.b'})
    bf1: PU = field(metadata={'xpath': 'cim:GovGASTWD.bf1'})
    bf2: PU = field(metadata={'xpath': 'cim:GovGASTWD.bf2'})
    c: Simple_Float = field(metadata={'xpath': 'cim:GovGASTWD.c'})
    cf2: PU = field(metadata={'xpath': 'cim:GovGASTWD.cf2'})
    ecr: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.ecr'})
    etd: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.etd'})
    k3: PU = field(metadata={'xpath': 'cim:GovGASTWD.k3'})
    k4: PU = field(metadata={'xpath': 'cim:GovGASTWD.k4'})
    k5: PU = field(metadata={'xpath': 'cim:GovGASTWD.k5'})
    k6: PU = field(metadata={'xpath': 'cim:GovGASTWD.k6'})
    kd: PU = field(metadata={'xpath': 'cim:GovGASTWD.kd'})
    kdroop: PU = field(metadata={'xpath': 'cim:GovGASTWD.kdroop'})
    kf: PU = field(metadata={'xpath': 'cim:GovGASTWD.kf'})
    ki: PU = field(metadata={'xpath': 'cim:GovGASTWD.ki'})
    kp: PU = field(metadata={'xpath': 'cim:GovGASTWD.kp'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovGASTWD.mwbase'})
    t: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.t'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.t5'})
    tc: Temperature = field(metadata={'xpath': 'cim:GovGASTWD.tc'})
    tcd: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.tcd'})
    td: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.td'})
    tf: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.tf'})
    tmax: PU = field(metadata={'xpath': 'cim:GovGASTWD.tmax'})
    tmin: PU = field(metadata={'xpath': 'cim:GovGASTWD.tmin'})
    tr: Temperature = field(metadata={'xpath': 'cim:GovGASTWD.tr'})
    trate: ActivePower = field(metadata={'xpath': 'cim:GovGASTWD.trate'})
    tt: Seconds = field(metadata={'xpath': 'cim:GovGASTWD.tt'})
