from __future__ import annotations
from ..Core.Curve import Curve
from .GeneratingUnit import GeneratingUnit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GrossToNetActivePowerCurve(Curve):
    GeneratingUnit_id: str | None = field(default=None, metadata={"xpath": "cim:GrossToNetActivePowerCurve.GeneratingUnit/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    GeneratingUnit_ref: GeneratingUnit = None
