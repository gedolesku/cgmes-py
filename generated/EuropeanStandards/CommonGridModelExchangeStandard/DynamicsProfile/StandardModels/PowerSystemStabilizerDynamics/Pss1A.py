from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .InputSignalKind import InputSignalKind
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Pss1A(PowerSystemStabilizerDynamics):
    a1: PU = field(metadata={'xpath': 'cim:Pss1A.a1'})
    a2: PU = field(metadata={'xpath': 'cim:Pss1A.a2'})
    a3: PU = field(metadata={'xpath': 'cim:Pss1A.a3'})
    a4: PU = field(metadata={'xpath': 'cim:Pss1A.a4'})
    a5: PU = field(metadata={'xpath': 'cim:Pss1A.a5'})
    a6: PU = field(metadata={'xpath': 'cim:Pss1A.a6'})
    a7: PU = field(metadata={'xpath': 'cim:Pss1A.a7'})
    a8: PU = field(metadata={'xpath': 'cim:Pss1A.a8'})
    inputSignalType: InputSignalKind = field(metadata={'xpath': 'cim:Pss1A.inputSignalType'})
    kd: Boolean = field(metadata={'xpath': 'cim:Pss1A.kd'})
    ks: PU = field(metadata={'xpath': 'cim:Pss1A.ks'})
    t1: Seconds = field(metadata={'xpath': 'cim:Pss1A.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:Pss1A.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:Pss1A.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:Pss1A.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:Pss1A.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:Pss1A.t6'})
    tdelay: Seconds = field(metadata={'xpath': 'cim:Pss1A.tdelay'})
    vcl: PU = field(metadata={'xpath': 'cim:Pss1A.vcl'})
    vcu: PU = field(metadata={'xpath': 'cim:Pss1A.vcu'})
    vrmax: PU = field(metadata={'xpath': 'cim:Pss1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:Pss1A.vrmin'})
