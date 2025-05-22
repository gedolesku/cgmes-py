from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class AsynchronousMachineKind(Enum):
    """Kind of Asynchronous Machine.
    """
    # The Asynchronous Machine is a generator.
    generator = auto()
    # The Asynchronous Machine is a motor.
    motor = auto()