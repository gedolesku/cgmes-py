from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class DCPolarityKind(Enum):
    """Polarity for DC circuits.
    """
    # Positive pole.
    positive = auto()
    # Middle pole, potentially grounded.
    middle = auto()
    # Negative pole.
    negative = auto()