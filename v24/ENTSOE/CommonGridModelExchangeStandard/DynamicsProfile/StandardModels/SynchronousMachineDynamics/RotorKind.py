from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class RotorKind(Enum):
    """Type of rotor on physical machine.
    """
    # Round rotor type of synchronous machine.
    roundRotor = auto()
    # Salient pole type of synchronous machine.
    salientPole = auto()