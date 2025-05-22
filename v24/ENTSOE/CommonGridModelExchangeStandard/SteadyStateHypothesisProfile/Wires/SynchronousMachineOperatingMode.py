from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class SynchronousMachineOperatingMode(Enum):
    """Synchronous machine operating mode.
    """
    generator = auto()
    condenser = auto()
    motor = auto()