from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.EnergyConsumer import EnergyConsumer

@dataclass
class ConformLoad(EnergyConsumer):
    """ConformLoad represent loads that follow a daily load change pattern where the
    pattern can be used to scale the load with a system load.
    """
    pass
