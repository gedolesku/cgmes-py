from __future__ import annotations
from ..Wires.EnergyConsumer import EnergyConsumer
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class StationSupply(EnergyConsumer):
    pass
