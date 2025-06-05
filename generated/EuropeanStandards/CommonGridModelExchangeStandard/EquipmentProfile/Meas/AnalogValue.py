from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from .Analog import Analog
from .MeasurementValue import MeasurementValue
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AnalogValue(MeasurementValue):
    value: Simple_Float = field(metadata={'xpath': 'cim:AnalogValue.value'})
    Analog_id: str | None = field(default=None, metadata={"xpath": "cim:AnalogValue.Analog/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Analog_ref: Analog = None
