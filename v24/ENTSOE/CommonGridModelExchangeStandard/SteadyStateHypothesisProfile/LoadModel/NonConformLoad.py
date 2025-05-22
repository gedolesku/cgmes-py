from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.EnergyConsumer import EnergyConsumer

@dataclass
class NonConformLoad(EnergyConsumer):
    """NonConformLoad represent loads that do not follow a daily load change pattern
    and changes are not correlated with the daily load change pattern.
    """
    pass
