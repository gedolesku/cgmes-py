from __future__ import annotations
from .WindContPType4bIEC import WindContPType4bIEC
from .WindGenType4IEC import WindGenType4IEC
from .WindMechIEC import WindMechIEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindTurbineType4bIEC(WindGenType4IEC):
    WindMechIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindTurbineType4bIEC.WindMechIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindMechIEC_ref: WindMechIEC = None
    WindContPType4bIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindTurbineType4bIEC.WindContPType4bIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindContPType4bIEC_ref: WindContPType4bIEC = None
