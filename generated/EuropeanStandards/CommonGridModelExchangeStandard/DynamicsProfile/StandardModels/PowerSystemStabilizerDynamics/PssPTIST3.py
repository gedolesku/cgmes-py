from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssPTIST3(PowerSystemStabilizerDynamics):
    a0: PU = field(metadata={'xpath': 'cim:PssPTIST3.a0'})
    a1: PU = field(metadata={'xpath': 'cim:PssPTIST3.a1'})
    a2: PU = field(metadata={'xpath': 'cim:PssPTIST3.a2'})
    a3: PU = field(metadata={'xpath': 'cim:PssPTIST3.a3'})
    a4: PU = field(metadata={'xpath': 'cim:PssPTIST3.a4'})
    a5: PU = field(metadata={'xpath': 'cim:PssPTIST3.a5'})
    al: PU = field(metadata={'xpath': 'cim:PssPTIST3.al'})
    athres: PU = field(metadata={'xpath': 'cim:PssPTIST3.athres'})
    b0: PU = field(metadata={'xpath': 'cim:PssPTIST3.b0'})
    b1: PU = field(metadata={'xpath': 'cim:PssPTIST3.b1'})
    b2: PU = field(metadata={'xpath': 'cim:PssPTIST3.b2'})
    b3: PU = field(metadata={'xpath': 'cim:PssPTIST3.b3'})
    b4: PU = field(metadata={'xpath': 'cim:PssPTIST3.b4'})
    b5: PU = field(metadata={'xpath': 'cim:PssPTIST3.b5'})
    dl: PU = field(metadata={'xpath': 'cim:PssPTIST3.dl'})
    dtc: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.dtc'})
    dtf: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.dtf'})
    dtp: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.dtp'})
    isw: Boolean = field(metadata={'xpath': 'cim:PssPTIST3.isw'})
    k: PU = field(metadata={'xpath': 'cim:PssPTIST3.k'})
    lthres: PU = field(metadata={'xpath': 'cim:PssPTIST3.lthres'})
    m: PU = field(metadata={'xpath': 'cim:PssPTIST3.m'})
    nav: Simple_Float = field(metadata={'xpath': 'cim:PssPTIST3.nav'})
    ncl: Simple_Float = field(metadata={'xpath': 'cim:PssPTIST3.ncl'})
    ncr: Simple_Float = field(metadata={'xpath': 'cim:PssPTIST3.ncr'})
    pmin: PU = field(metadata={'xpath': 'cim:PssPTIST3.pmin'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.t6'})
    tf: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.tf'})
    tp: Seconds = field(metadata={'xpath': 'cim:PssPTIST3.tp'})
