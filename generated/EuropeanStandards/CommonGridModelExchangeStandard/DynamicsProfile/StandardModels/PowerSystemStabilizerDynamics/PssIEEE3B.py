from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .InputSignalKind import InputSignalKind
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssIEEE3B(PowerSystemStabilizerDynamics):
    a1: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a1'})
    a2: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a2'})
    a3: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a3'})
    a4: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a4'})
    a5: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a5'})
    a6: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a6'})
    a7: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a7'})
    a8: PU = field(metadata={'xpath': 'cim:PssIEEE3B.a8'})
    inputSignal1Type: InputSignalKind = field(metadata={'xpath': 'cim:PssIEEE3B.inputSignal1Type'})
    inputSignal2Type: InputSignalKind = field(metadata={'xpath': 'cim:PssIEEE3B.inputSignal2Type'})
    ks1: PU = field(metadata={'xpath': 'cim:PssIEEE3B.ks1'})
    ks2: PU = field(metadata={'xpath': 'cim:PssIEEE3B.ks2'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssIEEE3B.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssIEEE3B.t2'})
    tw1: Seconds = field(metadata={'xpath': 'cim:PssIEEE3B.tw1'})
    tw2: Seconds = field(metadata={'xpath': 'cim:PssIEEE3B.tw2'})
    tw3: Seconds = field(metadata={'xpath': 'cim:PssIEEE3B.tw3'})
    vstmax: PU = field(metadata={'xpath': 'cim:PssIEEE3B.vstmax'})
    vstmin: PU = field(metadata={'xpath': 'cim:PssIEEE3B.vstmin'})
