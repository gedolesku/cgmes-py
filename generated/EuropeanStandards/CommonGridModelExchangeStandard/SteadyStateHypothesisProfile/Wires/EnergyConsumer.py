from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ReactivePower import ReactivePower
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class EnergyConsumer(ConductingEquipment):
    p: ActivePower = field(metadata={'xpath': 'cim:EnergyConsumer.p'})
    q: ReactivePower = field(metadata={'xpath': 'cim:EnergyConsumer.q'})
