from __future__ import annotations
from .DCConductingEquipment import DCConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCChopper(DCConductingEquipment):
    pass
