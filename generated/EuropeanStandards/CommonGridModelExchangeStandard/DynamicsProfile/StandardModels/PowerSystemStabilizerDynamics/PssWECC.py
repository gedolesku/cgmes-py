from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .InputSignalKind import InputSignalKind
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssWECC(PowerSystemStabilizerDynamics):
    inputSignal1Type: InputSignalKind = field(metadata={'xpath': 'cim:PssWECC.inputSignal1Type'})
    inputSignal2Type: InputSignalKind = field(metadata={'xpath': 'cim:PssWECC.inputSignal2Type'})
    k1: PU = field(metadata={'xpath': 'cim:PssWECC.k1'})
    k2: PU = field(metadata={'xpath': 'cim:PssWECC.k2'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssWECC.t1'})
    t10: Seconds = field(metadata={'xpath': 'cim:PssWECC.t10'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssWECC.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:PssWECC.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:PssWECC.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:PssWECC.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:PssWECC.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:PssWECC.t7'})
    t8: Seconds = field(metadata={'xpath': 'cim:PssWECC.t8'})
    t9: Seconds = field(metadata={'xpath': 'cim:PssWECC.t9'})
    vcl: PU = field(metadata={'xpath': 'cim:PssWECC.vcl'})
    vcu: PU = field(metadata={'xpath': 'cim:PssWECC.vcu'})
    vsmax: PU = field(metadata={'xpath': 'cim:PssWECC.vsmax'})
    vsmin: PU = field(metadata={'xpath': 'cim:PssWECC.vsmin'})
