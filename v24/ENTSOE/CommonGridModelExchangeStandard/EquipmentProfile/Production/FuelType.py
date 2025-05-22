from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class FuelType(Enum):
    """Type of fuel.
    """
    # Generic coal, not including lignite type.
    coal = auto()
    # Oil.
    oil = auto()
    # Natural gas.
    gas = auto()
    # The fuel is lignite coal.  Note that this is a special type of coal, so the
    # other enum of coal is reserved for hard coal types or if the exact type of coal
    # is not known.
    lignite = auto()
    # Hard coal
    hardCoal = auto()
    # Oil Shale
    oilShale = auto()