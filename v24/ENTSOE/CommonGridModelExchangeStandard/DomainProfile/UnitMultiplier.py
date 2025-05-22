from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class UnitMultiplier(Enum):
    """The unit multipliers defined for the CIM.
    """
    # Pico 10**-12.
    p = auto()
    # Nano 10**-9.
    n = auto()
    # Micro 10**-6.
    micro = auto()
    # Milli 10**-3.
    m = auto()
    # Centi 10**-2.
    c = auto()
    # Deci 10**-1.
    d = auto()
    # Kilo 10**3.
    k = auto()
    # Mega 10**6.
    M = auto()
    # Giga 10**9.
    G = auto()
    # Tera 10**12.
    T = auto()
    # No multiplier or equivalently multiply by 1.
    none = auto()