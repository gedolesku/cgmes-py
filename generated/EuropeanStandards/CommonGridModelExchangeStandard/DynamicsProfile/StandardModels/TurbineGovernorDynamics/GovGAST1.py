from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Frequency import Frequency
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovGAST1(TurbineGovernorDynamics):
    a: Simple_Float = field(metadata={'xpath': 'cim:GovGAST1.a'})
    b: Simple_Float = field(metadata={'xpath': 'cim:GovGAST1.b'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovGAST1.db1'})
    db2: ActivePower = field(metadata={'xpath': 'cim:GovGAST1.db2'})
    eps: Frequency = field(metadata={'xpath': 'cim:GovGAST1.eps'})
    fidle: PU = field(metadata={'xpath': 'cim:GovGAST1.fidle'})
    gv1: PU = field(metadata={'xpath': 'cim:GovGAST1.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovGAST1.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovGAST1.gv3'})
    gv4: PU = field(metadata={'xpath': 'cim:GovGAST1.gv4'})
    gv5: PU = field(metadata={'xpath': 'cim:GovGAST1.gv5'})
    gv6: PU = field(metadata={'xpath': 'cim:GovGAST1.gv6'})
    ka: PU = field(metadata={'xpath': 'cim:GovGAST1.ka'})
    kt: PU = field(metadata={'xpath': 'cim:GovGAST1.kt'})
    lmax: PU = field(metadata={'xpath': 'cim:GovGAST1.lmax'})
    loadinc: PU = field(metadata={'xpath': 'cim:GovGAST1.loadinc'})
    ltrate: Simple_Float = field(metadata={'xpath': 'cim:GovGAST1.ltrate'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovGAST1.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovGAST1.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovGAST1.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovGAST1.pgv3'})
    pgv4: PU = field(metadata={'xpath': 'cim:GovGAST1.pgv4'})
    pgv5: PU = field(metadata={'xpath': 'cim:GovGAST1.pgv5'})
    pgv6: PU = field(metadata={'xpath': 'cim:GovGAST1.pgv6'})
    r: PU = field(metadata={'xpath': 'cim:GovGAST1.r'})
    rmax: Simple_Float = field(metadata={'xpath': 'cim:GovGAST1.rmax'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovGAST1.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovGAST1.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovGAST1.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovGAST1.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:GovGAST1.t5'})
    tltr: Seconds = field(metadata={'xpath': 'cim:GovGAST1.tltr'})
    vmax: PU = field(metadata={'xpath': 'cim:GovGAST1.vmax'})
    vmin: PU = field(metadata={'xpath': 'cim:GovGAST1.vmin'})
