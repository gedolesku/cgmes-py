from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class OrientationKind(Enum):
    """The orientation of the coordinate system with respect to top, left, and the
    coordinate number system.
    """
    # For 2D diagrams, a negative orientation gives the left-hand orientation
    # (favoured by computer graphics displays) with X values increasing from left to
    # right and Y values increasing from top to bottom.   This is also known as a
    # left hand orientation.
    negative = auto()