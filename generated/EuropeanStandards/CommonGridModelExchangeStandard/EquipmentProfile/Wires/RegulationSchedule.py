from __future__ import annotations
from ..LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
from .RegulatingControl import RegulatingControl
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class RegulationSchedule(SeasonDayTypeSchedule):
    RegulatingControl_id: str | None = field(default=None, metadata={"xpath": "cim:RegulationSchedule.RegulatingControl/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    RegulatingControl_ref: RegulatingControl = None
