from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .InputSignalKind import InputSignalKind
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Pss2ST(PowerSystemStabilizerDynamics):
    inputSignal1Type: InputSignalKind = field(metadata={'xpath': 'cim:Pss2ST.inputSignal1Type'})
    inputSignal2Type: InputSignalKind = field(metadata={'xpath': 'cim:Pss2ST.inputSignal2Type'})
    k1: PU = field(metadata={'xpath': 'cim:Pss2ST.k1'})
    k2: PU = field(metadata={'xpath': 'cim:Pss2ST.k2'})
    lsmax: PU = field(metadata={'xpath': 'cim:Pss2ST.lsmax'})
    lsmin: PU = field(metadata={'xpath': 'cim:Pss2ST.lsmin'})
    t1: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t1'})
    t10: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t10'})
    t2: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t7'})
    t8: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t8'})
    t9: Seconds = field(metadata={'xpath': 'cim:Pss2ST.t9'})
    vcl: PU = field(metadata={'xpath': 'cim:Pss2ST.vcl'})
    vcu: PU = field(metadata={'xpath': 'cim:Pss2ST.vcu'})
