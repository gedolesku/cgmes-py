from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssPTIST1(PowerSystemStabilizerDynamics):
    dtc: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.dtc'})
    dtf: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.dtf'})
    dtp: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.dtp'})
    k: PU = field(metadata={'xpath': 'cim:PssPTIST1.k'})
    m: PU = field(metadata={'xpath': 'cim:PssPTIST1.m'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.t4'})
    tf: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.tf'})
    tp: Seconds = field(metadata={'xpath': 'cim:PssPTIST1.tp'})
