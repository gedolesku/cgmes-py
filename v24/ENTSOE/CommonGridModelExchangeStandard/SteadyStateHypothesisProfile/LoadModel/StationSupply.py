from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.EnergyConsumer import EnergyConsumer

@dataclass
class StationSupply(EnergyConsumer):
    """Station supply with load derived from the station output.
    """
    pass
