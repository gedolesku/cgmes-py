from __future__ import annotations
from .RatioTapChangerTable import RatioTapChangerTable
from .TapChangerTablePoint import TapChangerTablePoint
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class RatioTapChangerTablePoint(TapChangerTablePoint):
    RatioTapChangerTable_id: str | None = field(default=None, metadata={"xpath": "cim:RatioTapChangerTablePoint.RatioTapChangerTable/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    RatioTapChangerTable_ref: RatioTapChangerTable = None
