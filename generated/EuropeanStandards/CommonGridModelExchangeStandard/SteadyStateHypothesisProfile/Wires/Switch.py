from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Switch(ConductingEquipment):
    open: Boolean = field(metadata={'xpath': 'cim:Switch.open'})
