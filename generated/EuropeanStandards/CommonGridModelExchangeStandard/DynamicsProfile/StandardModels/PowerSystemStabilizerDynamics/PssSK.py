from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssSK(PowerSystemStabilizerDynamics):
    k1: PU = field(metadata={'xpath': 'cim:PssSK.k1'})
    k2: PU = field(metadata={'xpath': 'cim:PssSK.k2'})
    k3: PU = field(metadata={'xpath': 'cim:PssSK.k3'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssSK.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssSK.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:PssSK.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:PssSK.t4'})
    t5: Seconds = field(metadata={'xpath': 'cim:PssSK.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:PssSK.t6'})
    vsmax: PU = field(metadata={'xpath': 'cim:PssSK.vsmax'})
    vsmin: PU = field(metadata={'xpath': 'cim:PssSK.vsmin'})
