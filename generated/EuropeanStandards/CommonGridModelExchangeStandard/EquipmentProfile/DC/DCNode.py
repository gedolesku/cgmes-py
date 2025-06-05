from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .DCEquipmentContainer import DCEquipmentContainer
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCNode(IdentifiedObject):
    DCEquipmentContainer_id: str | None = field(default=None, metadata={"xpath": "cim:DCNode.DCEquipmentContainer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    DCEquipmentContainer_ref: DCEquipmentContainer = None
