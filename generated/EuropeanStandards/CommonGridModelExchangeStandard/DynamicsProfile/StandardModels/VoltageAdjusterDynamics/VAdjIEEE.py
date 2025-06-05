from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .VoltageAdjusterDynamics import VoltageAdjusterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VAdjIEEE(VoltageAdjusterDynamics):
    adjslew: Simple_Float = field(metadata={'xpath': 'cim:VAdjIEEE.adjslew'})
    taoff: Seconds = field(metadata={'xpath': 'cim:VAdjIEEE.taoff'})
    taon: Seconds = field(metadata={'xpath': 'cim:VAdjIEEE.taon'})
    vadjf: Simple_Float = field(metadata={'xpath': 'cim:VAdjIEEE.vadjf'})
    vadjmax: PU = field(metadata={'xpath': 'cim:VAdjIEEE.vadjmax'})
    vadjmin: PU = field(metadata={'xpath': 'cim:VAdjIEEE.vadjmin'})
