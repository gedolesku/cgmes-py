from __future__ import annotations
from .EnergyArea import EnergyArea
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LoadArea(EnergyArea):
    pass
