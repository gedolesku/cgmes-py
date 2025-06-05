from __future__ import annotations
from ..LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
from .TapChanger import TapChanger
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TapSchedule(SeasonDayTypeSchedule):
    TapChanger_id: str | None = field(default=None, metadata={"xpath": "cim:TapSchedule.TapChanger/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TapChanger_ref: TapChanger = None
