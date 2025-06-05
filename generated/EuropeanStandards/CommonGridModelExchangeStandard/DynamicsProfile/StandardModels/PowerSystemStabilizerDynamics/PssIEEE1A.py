from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .InputSignalKind import InputSignalKind
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssIEEE1A(PowerSystemStabilizerDynamics):
    a1: PU = field(metadata={'xpath': 'cim:PssIEEE1A.a1'})
    a2: PU = field(metadata={'xpath': 'cim:PssIEEE1A.a2'})
    inputSignalType: InputSignalKind = field(metadata={'xpath': 'cim:PssIEEE1A.inputSignalType'})
    ks: PU = field(metadata={'xpath': 'cim:PssIEEE1A.ks'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssIEEE1A.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssIEEE1A.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:PssIEEE1A.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:PssIEEE1A.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:PssIEEE1A.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:PssIEEE1A.t6'})
    vrmax: PU = field(metadata={'xpath': 'cim:PssIEEE1A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:PssIEEE1A.vrmin'})
