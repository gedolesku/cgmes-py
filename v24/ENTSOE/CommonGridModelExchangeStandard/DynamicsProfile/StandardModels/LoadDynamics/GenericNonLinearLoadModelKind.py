from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class GenericNonLinearLoadModelKind(Enum):
    """Type of generic non-linear load model.
    """
    # Exponential recovery model.
    exponentialRecovery = auto()
    # Load adaptive model.
    loadAdaptive = auto()