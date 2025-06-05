from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.CurrentFlow import CurrentFlow
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Switch(ConductingEquipment):
    normalOpen: Boolean = field(metadata={'xpath': 'cim:Switch.normalOpen'})
    retained: Boolean = field(metadata={'xpath': 'cim:Switch.retained'})
    ratedCurrent: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:Switch.ratedCurrent'})
