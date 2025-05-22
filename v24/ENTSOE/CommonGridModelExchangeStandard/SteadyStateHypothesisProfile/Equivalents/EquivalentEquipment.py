from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class EquivalentEquipment(ConductingEquipment):
    """The class represents equivalent objects that are the result of a network
    reduction. The class is the base for equivalent objects of different types.
    """
    pass
