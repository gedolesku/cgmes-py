from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from .AnalogLimitSet import AnalogLimitSet
from .Limit import Limit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AnalogLimit(Limit):
    value: Simple_Float = field(metadata={'xpath': 'cim:AnalogLimit.value'})
    LimitSet_id: str | None = field(default=None, metadata={"xpath": "cim:AnalogLimit.LimitSet/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LimitSet_ref: AnalogLimitSet = None
