from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from ..Core.Equipment import Equipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GeneratingUnit(Equipment):
    normalPF: Simple_Float = field(metadata={'xpath': 'cim:GeneratingUnit.normalPF'})
