from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Ground(ConductingEquipment):
    pass
