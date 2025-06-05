from __future__ import annotations
from ...DomainProfile.Conductance import Conductance
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Susceptance import Susceptance
from ...DomainProfile.Temperature import Temperature
from .Conductor import Conductor
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ACLineSegment(Conductor):
    b0ch: Susceptance = field(metadata={'xpath': 'cim:ACLineSegment.b0ch'})
    bch: Susceptance = field(metadata={'xpath': 'cim:ACLineSegment.bch'})
    g0ch: Conductance = field(metadata={'xpath': 'cim:ACLineSegment.g0ch'})
    r: Resistance = field(metadata={'xpath': 'cim:ACLineSegment.r'})
    r0: Resistance = field(metadata={'xpath': 'cim:ACLineSegment.r0'})
    shortCircuitEndTemperature: Temperature = field(metadata={'xpath': 'cim:ACLineSegment.shortCircuitEndTemperature'})
    x: Reactance = field(metadata={'xpath': 'cim:ACLineSegment.x'})
    x0: Reactance = field(metadata={'xpath': 'cim:ACLineSegment.x0'})
    gch: Optional[Conductance] = field(default=None, metadata={'xpath': 'cim:ACLineSegment.gch'})
