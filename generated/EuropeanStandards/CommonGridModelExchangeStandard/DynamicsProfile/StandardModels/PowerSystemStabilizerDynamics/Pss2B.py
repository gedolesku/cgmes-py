from __future__ import annotations
from ....DomainProfile.Integer import Integer
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .InputSignalKind import InputSignalKind
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Pss2B(PowerSystemStabilizerDynamics):
    a: Simple_Float = field(metadata={'xpath': 'cim:Pss2B.a'})
    inputSignal1Type: InputSignalKind = field(metadata={'xpath': 'cim:Pss2B.inputSignal1Type'})
    inputSignal2Type: InputSignalKind = field(metadata={'xpath': 'cim:Pss2B.inputSignal2Type'})
    ks1: PU = field(metadata={'xpath': 'cim:Pss2B.ks1'})
    ks2: PU = field(metadata={'xpath': 'cim:Pss2B.ks2'})
    ks3: PU = field(metadata={'xpath': 'cim:Pss2B.ks3'})
    ks4: PU = field(metadata={'xpath': 'cim:Pss2B.ks4'})
    m: Integer = field(metadata={'xpath': 'cim:Pss2B.m'})
    n: Integer = field(metadata={'xpath': 'cim:Pss2B.n'})
    t1: Seconds = field(metadata={'xpath': 'cim:Pss2B.t1'})
    t10: Seconds = field(metadata={'xpath': 'cim:Pss2B.t10'})
    t11: Seconds = field(metadata={'xpath': 'cim:Pss2B.t11'})
    t2: Seconds = field(metadata={'xpath': 'cim:Pss2B.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:Pss2B.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:Pss2B.t4'})
    t6: Seconds = field(metadata={'xpath': 'cim:Pss2B.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:Pss2B.t7'})
    t8: Seconds = field(metadata={'xpath': 'cim:Pss2B.t8'})
    t9: Seconds = field(metadata={'xpath': 'cim:Pss2B.t9'})
    ta: Seconds = field(metadata={'xpath': 'cim:Pss2B.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:Pss2B.tb'})
    tw1: Seconds = field(metadata={'xpath': 'cim:Pss2B.tw1'})
    tw2: Seconds = field(metadata={'xpath': 'cim:Pss2B.tw2'})
    tw3: Seconds = field(metadata={'xpath': 'cim:Pss2B.tw3'})
    tw4: Seconds = field(metadata={'xpath': 'cim:Pss2B.tw4'})
    vsi1max: PU = field(metadata={'xpath': 'cim:Pss2B.vsi1max'})
    vsi1min: PU = field(metadata={'xpath': 'cim:Pss2B.vsi1min'})
    vsi2max: PU = field(metadata={'xpath': 'cim:Pss2B.vsi2max'})
    vsi2min: PU = field(metadata={'xpath': 'cim:Pss2B.vsi2min'})
    vstmax: PU = field(metadata={'xpath': 'cim:Pss2B.vstmax'})
    vstmin: PU = field(metadata={'xpath': 'cim:Pss2B.vstmin'})
