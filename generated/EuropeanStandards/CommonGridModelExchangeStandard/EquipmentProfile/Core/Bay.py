from __future__ import annotations
from .EquipmentContainer import EquipmentContainer
from .VoltageLevel import VoltageLevel
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Bay(EquipmentContainer):
    VoltageLevel_id: str | None = field(default=None, metadata={"xpath": "cim:Bay.VoltageLevel/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    VoltageLevel_ref: VoltageLevel = None
