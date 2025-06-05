from __future__ import annotations
from .ConformLoadGroup import ConformLoadGroup
from .SeasonDayTypeSchedule import SeasonDayTypeSchedule
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ConformLoadSchedule(SeasonDayTypeSchedule):
    ConformLoadGroup_id: str | None = field(default=None, metadata={"xpath": "cim:ConformLoadSchedule.ConformLoadGroup/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConformLoadGroup_ref: ConformLoadGroup = None
