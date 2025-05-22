from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class WindingConnection(Enum):
    """Winding connection type.
    """
    # Delta
    D = auto()
    # Wye
    Y = auto()
    # ZigZag
    Z = auto()
    # Wye, with neutral brought out for grounding.
    Yn = auto()
    # ZigZag, with neutral brought out for grounding.
    Zn = auto()
    # Autotransformer common winding
    A = auto()
    # Independent winding, for single-phase connections
    I = auto()