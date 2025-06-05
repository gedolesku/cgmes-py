from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PssELIN2(PowerSystemStabilizerDynamics):
    apss: PU = field(metadata={'xpath': 'cim:PssELIN2.apss'})
    ks1: PU = field(metadata={'xpath': 'cim:PssELIN2.ks1'})
    ks2: PU = field(metadata={'xpath': 'cim:PssELIN2.ks2'})
    ppss: PU = field(metadata={'xpath': 'cim:PssELIN2.ppss'})
    psslim: PU = field(metadata={'xpath': 'cim:PssELIN2.psslim'})
    ts1: Seconds = field(metadata={'xpath': 'cim:PssELIN2.ts1'})
    ts2: Seconds = field(metadata={'xpath': 'cim:PssELIN2.ts2'})
    ts3: Seconds = field(metadata={'xpath': 'cim:PssELIN2.ts3'})
    ts4: Seconds = field(metadata={'xpath': 'cim:PssELIN2.ts4'})
    ts5: Seconds = field(metadata={'xpath': 'cim:PssELIN2.ts5'})
    ts6: Seconds = field(metadata={'xpath': 'cim:PssELIN2.ts6'})
