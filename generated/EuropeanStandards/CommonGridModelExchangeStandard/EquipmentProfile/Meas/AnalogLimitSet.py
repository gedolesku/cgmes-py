from __future__ import annotations
from .Analog import Analog
from .LimitSet import LimitSet
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class AnalogLimitSet(LimitSet):
    Measurements_id: list[str] | None = field(default_factory=list, metadata={"xpath": "cim:AnalogLimitSet.Measurements/@rdf:resource", "pattern": r"^#.+$"})
    Measurements_ref: Analog | None = None
