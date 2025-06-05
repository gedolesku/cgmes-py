from __future__ import annotations
from ...DomainProfile.Conductance import Conductance
from ...DomainProfile.Susceptance import Susceptance
from .ShuntCompensator import ShuntCompensator
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LinearShuntCompensator(ShuntCompensator):
    b0PerSection: Susceptance = field(metadata={'xpath': 'cim:LinearShuntCompensator.b0PerSection'})
    bPerSection: Susceptance = field(metadata={'xpath': 'cim:LinearShuntCompensator.bPerSection'})
    g0PerSection: Conductance = field(metadata={'xpath': 'cim:LinearShuntCompensator.g0PerSection'})
    gPerSection: Conductance = field(metadata={'xpath': 'cim:LinearShuntCompensator.gPerSection'})
