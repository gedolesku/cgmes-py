from __future__ import annotations
from ...DomainProfile.Integer import Integer
from .Discrete import Discrete
from .MeasurementValue import MeasurementValue
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DiscreteValue(MeasurementValue):
    value: Integer = field(metadata={'xpath': 'cim:DiscreteValue.value'})
    Discrete_id: str | None = field(default=None, metadata={"xpath": "cim:DiscreteValue.Discrete/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Discrete_ref: Discrete = None
