from __future__ import annotations
from ...DomainProfile.Integer import Integer
from .AccumulatorLimitSet import AccumulatorLimitSet
from .Limit import Limit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AccumulatorLimit(Limit):
    value: Integer = field(metadata={'xpath': 'cim:AccumulatorLimit.value'})
    LimitSet_id: str | None = field(default=None, metadata={"xpath": "cim:AccumulatorLimit.LimitSet/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LimitSet_ref: AccumulatorLimitSet = None
