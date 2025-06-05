from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .DCEquipmentContainer import DCEquipmentContainer
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCTopologicalNode(IdentifiedObject):
    DCEquipmentContainer_id: str | None = field(default=None, metadata={"xpath": "cim:DCTopologicalNode.DCEquipmentContainer/@rdf:resource", "pattern": r"^#.+$"})
    DCEquipmentContainer_ref: DCEquipmentContainer | None = None
