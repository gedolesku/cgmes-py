from __future__ import annotations
from ...DomainProfile.Conductance import Conductance
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Susceptance import Susceptance
from .NonlinearShuntCompensator import NonlinearShuntCompensator
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class NonlinearShuntCompensatorPoint:
    b: Susceptance = field(metadata={'xpath': 'cim:NonlinearShuntCompensatorPoint.b'})
    b0: Susceptance = field(metadata={'xpath': 'cim:NonlinearShuntCompensatorPoint.b0'})
    g: Conductance = field(metadata={'xpath': 'cim:NonlinearShuntCompensatorPoint.g'})
    g0: Conductance = field(metadata={'xpath': 'cim:NonlinearShuntCompensatorPoint.g0'})
    sectionNumber: Integer = field(metadata={'xpath': 'cim:NonlinearShuntCompensatorPoint.sectionNumber'})
    NonlinearShuntCompensator_id: str | None = field(default=None, metadata={"xpath": "cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    NonlinearShuntCompensator_ref: NonlinearShuntCompensator = None
