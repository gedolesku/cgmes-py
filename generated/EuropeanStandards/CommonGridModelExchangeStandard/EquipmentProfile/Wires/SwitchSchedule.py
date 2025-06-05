from __future__ import annotations
from ..LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
from .Switch import Switch
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SwitchSchedule(SeasonDayTypeSchedule):
    Switch_id: str | None = field(default=None, metadata={"xpath": "cim:SwitchSchedule.Switch/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Switch_ref: Switch = None
