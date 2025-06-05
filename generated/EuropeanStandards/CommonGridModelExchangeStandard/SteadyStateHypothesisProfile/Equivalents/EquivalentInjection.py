from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.ReactivePower import ReactivePower
from ...DomainProfile.Voltage import Voltage
from .EquivalentEquipment import EquivalentEquipment
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class EquivalentInjection(EquivalentEquipment):
    p: ActivePower = field(metadata={'xpath': 'cim:EquivalentInjection.p'})
    q: ReactivePower = field(metadata={'xpath': 'cim:EquivalentInjection.q'})
    regulationStatus: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:EquivalentInjection.regulationStatus'})
    regulationTarget: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:EquivalentInjection.regulationTarget'})
