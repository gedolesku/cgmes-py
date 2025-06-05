from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from ..Production.GeneratingUnit import GeneratingUnit
from .ControlArea import ControlArea
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ControlAreaGeneratingUnit(IdentifiedObject):
    ControlArea_id: str | None = field(default=None, metadata={"xpath": "cim:ControlAreaGeneratingUnit.ControlArea/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ControlArea_ref: ControlArea = None
    GeneratingUnit_id: str | None = field(default=None, metadata={"xpath": "cim:ControlAreaGeneratingUnit.GeneratingUnit/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    GeneratingUnit_ref: GeneratingUnit = None
