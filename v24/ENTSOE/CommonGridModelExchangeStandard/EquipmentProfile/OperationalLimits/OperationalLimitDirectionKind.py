from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class OperationalLimitDirectionKind(Enum):
    """The direction attribute describes the side of  a limit that is a violation.
    """
    # High means that a monitored value above the limit value is a violation.   If
    # applied to a terminal flow, the positive direction is into the terminal.
    high = auto()
    # Low means a monitored value below the limit is a violation.  If applied to a
    # terminal flow, the positive direction is into the terminal.
    low = auto()
    # An absoluteValue limit means that a monitored absolute value above the limit
    # value is a violation.
    absoluteValue = auto()