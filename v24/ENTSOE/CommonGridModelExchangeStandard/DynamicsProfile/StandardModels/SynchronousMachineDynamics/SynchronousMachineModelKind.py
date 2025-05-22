from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class SynchronousMachineModelKind(Enum):
    """Type of synchronous machine model used in Dynamic simulation applications.
    """
    # Subtransient synchronous machine model.
    subtransient = auto()
    # WECC Type F variant of subtransient synchronous machine model.
    subtransientTypeF = auto()
    # WECC Type J variant of subtransient synchronous machine model.
    subtransientTypeJ = auto()
    # Simplified version of subtransient synchronous machine model where magnetic
    # coupling between the direct and quadrature axes is ignored.
    subtransientSimplified = auto()
    # Simplified version of a subtransient synchronous machine model with no damper
    # circuit on d-axis. 
    subtransientSimplifiedDirectAxis = auto()