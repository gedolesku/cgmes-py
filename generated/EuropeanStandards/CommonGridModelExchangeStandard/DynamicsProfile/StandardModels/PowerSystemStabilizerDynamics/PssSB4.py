from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssSB4(PowerSystemStabilizerDynamics):
    kx: PU = field(metadata={'xpath': 'cim:PssSB4.kx'})
    ta: Seconds = field(metadata={'xpath': 'cim:PssSB4.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:PssSB4.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:PssSB4.tc'})
    td: Seconds = field(metadata={'xpath': 'cim:PssSB4.td'})
    te: Seconds = field(metadata={'xpath': 'cim:PssSB4.te'})
    tt: Seconds = field(metadata={'xpath': 'cim:PssSB4.tt'})
    tx1: Seconds = field(metadata={'xpath': 'cim:PssSB4.tx1'})
    tx2: Seconds = field(metadata={'xpath': 'cim:PssSB4.tx2'})
    vsmax: PU = field(metadata={'xpath': 'cim:PssSB4.vsmax'})
    vsmin: PU = field(metadata={'xpath': 'cim:PssSB4.vsmin'})
