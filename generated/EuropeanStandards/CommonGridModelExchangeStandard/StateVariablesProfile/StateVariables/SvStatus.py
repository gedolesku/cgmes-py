from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SvStatus:
    inService: Boolean = field(metadata={'xpath': 'cim:SvStatus.inService'})
    ConductingEquipment_id: str | None = field(default=None, metadata={"xpath": "cim:SvStatus.ConductingEquipment/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConductingEquipment_ref: ConductingEquipment = None
