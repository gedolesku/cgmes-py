from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class PetersenCoilModeKind(Enum):
    """The mode of operation for a Petersen coil.
    """
    # Fixed position.
    fixed = auto()
    # Manual positioning.
    manual = auto()
    # Automatic positioning.
    automaticPositioning = auto()