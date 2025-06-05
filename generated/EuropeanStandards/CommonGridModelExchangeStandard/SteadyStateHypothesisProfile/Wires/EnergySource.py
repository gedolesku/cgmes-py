from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ReactivePower import ReactivePower
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class EnergySource(ConductingEquipment):
    activePower: ActivePower = field(metadata={'xpath': 'cim:EnergySource.activePower'})
    reactivePower: ReactivePower = field(metadata={'xpath': 'cim:EnergySource.reactivePower'})
