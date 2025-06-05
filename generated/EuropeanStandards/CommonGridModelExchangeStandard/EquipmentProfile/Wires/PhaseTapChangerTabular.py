from __future__ import annotations
from .PhaseTapChanger import PhaseTapChanger
from .PhaseTapChangerTable import PhaseTapChangerTable
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class PhaseTapChangerTabular(PhaseTapChanger):
    PhaseTapChangerTable_id: str | None = field(default=None, metadata={"xpath": "cim:PhaseTapChangerTabular.PhaseTapChangerTable/@rdf:resource", "pattern": r"^#.+$"})
    PhaseTapChangerTable_ref: PhaseTapChangerTable | None = None
