from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class SynchronousMachineKind(Enum):
    """Synchronous machine type.
    """
    generator = auto()
    condenser = auto()
    generatorOrCondenser = auto()
    motor = auto()
    generatorOrMotor = auto()
    motorOrCondenser = auto()
    generatorOrCondenserOrMotor = auto()