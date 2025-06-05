from __future__ import annotations
from .WindContPType4aIEC import WindContPType4aIEC
from .WindGenType4IEC import WindGenType4IEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindTurbineType4aIEC(WindGenType4IEC):
    WindContPType4aIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindTurbineType4aIEC.WindContPType4aIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindContPType4aIEC_ref: WindContPType4aIEC = None
