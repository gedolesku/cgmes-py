from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from .Curve import Curve
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class CurveData:
    xvalue: Simple_Float = field(metadata={'xpath': 'cim:CurveData.xvalue'})
    y1value: Simple_Float = field(metadata={'xpath': 'cim:CurveData.y1value'})
    Curve_id: str | None = field(default=None, metadata={"xpath": "cim:CurveData.Curve/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Curve_ref: Curve = None
    y2value: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:CurveData.y2value'})
