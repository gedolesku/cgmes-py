from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class CurveStyle(Enum):
    """Style or shape of curve.
    """
    # The Y-axis values are assumed constant until the next curve point and prior to
    # the first curve point.
    constantYValue = auto()
    # The Y-axis values are assumed to be a straight line between values.  Also known
    # as linear interpolation.
    straightLineYValues = auto()