from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class DCConverterOperatingModeKind(Enum):
    """The operating mode of an HVDC bipole.
    """
    # Bipolar operation.
    bipolar = auto()
    # Monopolar operation with metallic return
    monopolarMetallicReturn = auto()
    # Monopolar operation with ground return
    monopolarGroundReturn = auto()