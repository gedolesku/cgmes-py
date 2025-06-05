from __future__ import annotations
from .NonConformLoadGroup import NonConformLoadGroup
from .SeasonDayTypeSchedule import SeasonDayTypeSchedule
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class NonConformLoadSchedule(SeasonDayTypeSchedule):
    NonConformLoadGroup_id: str | None = field(default=None, metadata={"xpath": "cim:NonConformLoadSchedule.NonConformLoadGroup/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    NonConformLoadGroup_ref: NonConformLoadGroup = None
