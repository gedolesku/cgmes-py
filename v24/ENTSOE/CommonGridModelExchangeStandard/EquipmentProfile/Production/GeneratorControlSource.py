from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class GeneratorControlSource(Enum):
    """The source of controls for a generating unit.
    """
    # Not available.
    unavailable = auto()
    # Off of automatic generation control (AGC).
    offAGC = auto()
    # On automatic generation control (AGC).
    onAGC = auto()
    # Plant is controlling.
    plantControl = auto()