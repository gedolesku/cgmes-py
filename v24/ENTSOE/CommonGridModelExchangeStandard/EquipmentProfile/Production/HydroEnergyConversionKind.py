from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class HydroEnergyConversionKind(Enum):
    """Specifies the capability of the hydro generating unit to convert energy as a
    generator or pump.
    """
    # Able to generate power, but not able to pump water for energy storage.
    generator = auto()
    # Able to both generate power and pump water for energy storage.
    pumpAndGenerator = auto()