from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class CsOperatingModeKind(Enum):
    """Operating mode for HVDC line operating as Current Source Converter.
    """
    # Operating as inverter
    inverter = auto()
    # Operating as rectifier.
    rectifier = auto()