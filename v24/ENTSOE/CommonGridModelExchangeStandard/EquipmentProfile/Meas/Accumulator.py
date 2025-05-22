from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Measurement import Measurement

@dataclass
class Accumulator(Measurement):
    """Accumulator represents an accumulated (counted) Measurement, e.g. an energy
    value.
    """
    pass
