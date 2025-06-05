from __future__ import annotations
from .WindContRotorRIEC import WindContRotorRIEC
from .WindPitchContEmulIEC import WindPitchContEmulIEC
from .WindTurbineType1or2IEC import WindTurbineType1or2IEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    WindContRotorRIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindGenTurbineType2IEC.WindContRotorRIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindContRotorRIEC_ref: WindContRotorRIEC = None
    WindPitchContEmulIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindGenTurbineType2IEC.WindPitchContEmulIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindPitchContEmulIEC_ref: WindPitchContEmulIEC = None
