from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class CsPpccControlKind(Enum):
    """Active power control modes for HVDC line operating as Current Source Converter.
    """
    # Active power control at AC side.
    activePower = auto()
    # DC voltage control.
    dcVoltage = auto()
    # DC current control
    dcCurrent = auto()