from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class TransformerControlMode(Enum):
    """Control modes for a transformer.
    """
    # Voltage control
    volt = auto()
    # Reactive power flow control
    reactive = auto()