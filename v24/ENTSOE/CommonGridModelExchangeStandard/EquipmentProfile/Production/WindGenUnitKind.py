from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class WindGenUnitKind(Enum):
    """Kind of wind generating unit.
    """
    # The wind generating unit is located offshore.
    offshore = auto()
    # The wind generating unit is located onshore.
    onshore = auto()