from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from ..Wires.ShuntCompensator import ShuntCompensator
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SvShuntCompensatorSections:
    sections: Simple_Float = field(metadata={'xpath': 'cim:SvShuntCompensatorSections.sections'})
    ShuntCompensator_id: str | None = field(default=None, metadata={"xpath": "cim:SvShuntCompensatorSections.ShuntCompensator/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ShuntCompensator_ref: ShuntCompensator = None
