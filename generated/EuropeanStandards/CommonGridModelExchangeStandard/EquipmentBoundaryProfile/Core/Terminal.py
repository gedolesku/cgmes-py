from __future__ import annotations
from .ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Terminal:
    ConductingEquipment_id: str | None = field(default=None, metadata={"xpath": "cim:Terminal.ConductingEquipment/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConductingEquipment_ref: ConductingEquipment = None
