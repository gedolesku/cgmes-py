from __future__ import annotations
from ....DomainProfile.Simple_Float import Simple_Float
from .MechanicalLoadDynamics import MechanicalLoadDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class MechLoad1(MechanicalLoadDynamics):
    a: Simple_Float = field(metadata={'xpath': 'cim:MechLoad1.a'})
    b: Simple_Float = field(metadata={'xpath': 'cim:MechLoad1.b'})
    d: Simple_Float = field(metadata={'xpath': 'cim:MechLoad1.d'})
    e: Simple_Float = field(metadata={'xpath': 'cim:MechLoad1.e'})
