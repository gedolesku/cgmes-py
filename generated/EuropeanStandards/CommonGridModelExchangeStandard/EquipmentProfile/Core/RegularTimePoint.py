from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Simple_Float import Simple_Float
from .RegularIntervalSchedule import RegularIntervalSchedule
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class RegularTimePoint:
    sequenceNumber: Integer = field(metadata={'xpath': 'cim:RegularTimePoint.sequenceNumber'})
    value1: Simple_Float = field(metadata={'xpath': 'cim:RegularTimePoint.value1'})
    IntervalSchedule_id: str | None = field(default=None, metadata={"xpath": "cim:RegularTimePoint.IntervalSchedule/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    IntervalSchedule_ref: RegularIntervalSchedule = None
    value2: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:RegularTimePoint.value2'})
