from __future__ import annotations
from .MeasurementValue import MeasurementValue
from .Quality61850 import Quality61850
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class MeasurementValueQuality(Quality61850):
    MeasurementValue_id: str | None = field(default=None, metadata={"xpath": "cim:MeasurementValueQuality.MeasurementValue/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    MeasurementValue_ref: MeasurementValue = None
