from __future__ import annotations
from ...DomainProfile.Conductance import Conductance
from ...DomainProfile.Susceptance import Susceptance
from .EquivalentEquipment import EquivalentEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class EquivalentShunt(EquivalentEquipment):
    b: Susceptance = field(metadata={'xpath': 'cim:EquivalentShunt.b'})
    g: Conductance = field(metadata={'xpath': 'cim:EquivalentShunt.g'})
