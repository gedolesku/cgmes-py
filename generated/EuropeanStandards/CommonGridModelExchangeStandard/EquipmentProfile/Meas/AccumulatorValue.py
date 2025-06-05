from __future__ import annotations
from ...DomainProfile.Integer import Integer
from .Accumulator import Accumulator
from .MeasurementValue import MeasurementValue
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AccumulatorValue(MeasurementValue):
    value: Integer = field(metadata={'xpath': 'cim:AccumulatorValue.value'})
    Accumulator_id: str | None = field(default=None, metadata={"xpath": "cim:AccumulatorValue.Accumulator/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Accumulator_ref: Accumulator = None
