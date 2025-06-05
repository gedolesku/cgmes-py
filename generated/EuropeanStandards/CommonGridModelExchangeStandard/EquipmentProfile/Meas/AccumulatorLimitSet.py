from __future__ import annotations
from .Accumulator import Accumulator
from .LimitSet import LimitSet
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class AccumulatorLimitSet(LimitSet):
    Measurements_id: list[str] | None = field(default_factory=list, metadata={"xpath": "cim:AccumulatorLimitSet.Measurements/@rdf:resource", "pattern": r"^#.+$"})
    Measurements_ref: Accumulator | None = None
