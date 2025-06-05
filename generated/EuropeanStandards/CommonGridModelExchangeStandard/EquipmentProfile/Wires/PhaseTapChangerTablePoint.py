from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from .PhaseTapChangerTable import PhaseTapChangerTable
from .TapChangerTablePoint import TapChangerTablePoint
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PhaseTapChangerTablePoint(TapChangerTablePoint):
    angle: AngleDegrees = field(metadata={'xpath': 'cim:PhaseTapChangerTablePoint.angle'})
    PhaseTapChangerTable_id: str | None = field(default=None, metadata={"xpath": "cim:PhaseTapChangerTablePoint.PhaseTapChangerTable/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    PhaseTapChangerTable_ref: PhaseTapChangerTable = None
