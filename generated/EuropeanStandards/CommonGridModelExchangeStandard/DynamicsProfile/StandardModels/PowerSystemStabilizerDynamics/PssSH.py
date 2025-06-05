from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssSH(PowerSystemStabilizerDynamics):
    k: PU = field(metadata={'xpath': 'cim:PssSH.k'})
    k0: PU = field(metadata={'xpath': 'cim:PssSH.k0'})
    k1: PU = field(metadata={'xpath': 'cim:PssSH.k1'})
    k2: PU = field(metadata={'xpath': 'cim:PssSH.k2'})
    k3: PU = field(metadata={'xpath': 'cim:PssSH.k3'})
    k4: PU = field(metadata={'xpath': 'cim:PssSH.k4'})
    t1: Seconds = field(metadata={'xpath': 'cim:PssSH.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:PssSH.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:PssSH.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:PssSH.t4'})
    td: Seconds = field(metadata={'xpath': 'cim:PssSH.td'})
    vsmax: PU = field(metadata={'xpath': 'cim:PssSH.vsmax'})
    vsmin: PU = field(metadata={'xpath': 'cim:PssSH.vsmin'})
