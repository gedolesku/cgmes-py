from __future__ import annotations
from ...DomainProfile.String import String
from .MeasurementValue import MeasurementValue
from .StringMeasurement import StringMeasurement
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class StringMeasurementValue(MeasurementValue):
    value: String = field(metadata={'xpath': 'cim:StringMeasurementValue.value'})
    StringMeasurement_id: str | None = field(default=None, metadata={"xpath": "cim:StringMeasurementValue.StringMeasurement/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    StringMeasurement_ref: StringMeasurement = None
