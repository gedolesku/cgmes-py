from __future__ import annotations
from .WindAeroConstIEC import WindAeroConstIEC
from .WindTurbineType1or2IEC import WindTurbineType1or2IEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindGenTurbineType1IEC(WindTurbineType1or2IEC):
    WindAeroConstIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindGenTurbineType1IEC.WindAeroConstIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindAeroConstIEC_ref: WindAeroConstIEC = None
