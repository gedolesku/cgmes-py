from __future__ import annotations
from .DCBaseTerminal import DCBaseTerminal
from .DCConductingEquipment import DCConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCTerminal(DCBaseTerminal):
    DCConductingEquipment_id: str | None = field(default=None, metadata={"xpath": "cim:DCTerminal.DCConductingEquipment/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    DCConductingEquipment_ref: DCConductingEquipment = None
