from __future__ import annotations
from ...DomainProfile.Inductance import Inductance
from ...DomainProfile.Resistance import Resistance
from .DCConductingEquipment import DCConductingEquipment
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCGround(DCConductingEquipment):
    inductance: Optional[Inductance] = field(default=None, metadata={'xpath': 'cim:DCGround.inductance'})
    r: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:DCGround.r'})
