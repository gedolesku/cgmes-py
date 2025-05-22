from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class ExcREXSFeedbackSignalKind(Enum):
    """Type of rate feedback signals.
    """
    # The voltage regulator output voltage is used. It is the same as exciter field
    # voltage.
    fieldVoltage = auto()
    # The exciter field current is used.
    fieldCurrent = auto()
    # The output voltage of the exciter is used.
    outputVoltage = auto()