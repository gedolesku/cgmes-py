from __future__ import annotations
from ...DomainProfile.Conductance import Conductance
from ...DomainProfile.Length import Length
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Susceptance import Susceptance
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.Terminal import Terminal
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class MutualCoupling(IdentifiedObject):
    b0ch: Susceptance = field(metadata={'xpath': 'cim:MutualCoupling.b0ch'})
    distance11: Length = field(metadata={'xpath': 'cim:MutualCoupling.distance11'})
    distance12: Length = field(metadata={'xpath': 'cim:MutualCoupling.distance12'})
    distance21: Length = field(metadata={'xpath': 'cim:MutualCoupling.distance21'})
    distance22: Length = field(metadata={'xpath': 'cim:MutualCoupling.distance22'})
    g0ch: Conductance = field(metadata={'xpath': 'cim:MutualCoupling.g0ch'})
    r0: Resistance = field(metadata={'xpath': 'cim:MutualCoupling.r0'})
    x0: Reactance = field(metadata={'xpath': 'cim:MutualCoupling.x0'})
    Second_Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:MutualCoupling.Second_Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Second_Terminal_ref: Terminal = None
    First_Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:MutualCoupling.First_Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    First_Terminal_ref: Terminal = None
