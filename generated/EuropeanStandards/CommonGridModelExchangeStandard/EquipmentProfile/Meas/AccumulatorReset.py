from __future__ import annotations
from .AccumulatorValue import AccumulatorValue
from .Control import Control
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AccumulatorReset(Control):
    AccumulatorValue_id: str | None = field(default=None, metadata={"xpath": "cim:AccumulatorReset.AccumulatorValue/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    AccumulatorValue_ref: AccumulatorValue = None
