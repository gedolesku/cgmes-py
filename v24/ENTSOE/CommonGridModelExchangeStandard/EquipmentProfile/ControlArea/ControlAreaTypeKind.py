from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class ControlAreaTypeKind(Enum):
    """The type of control area.
    """
    # Used for automatic generation control.
    AGC = auto()
    # Used for load forecast.
    Forecast = auto()
    # Used for interchange specification or control.
    Interchange = auto()