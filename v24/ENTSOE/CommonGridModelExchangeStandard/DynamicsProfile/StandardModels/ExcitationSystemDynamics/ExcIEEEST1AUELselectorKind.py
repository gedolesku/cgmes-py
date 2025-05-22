from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class ExcIEEEST1AUELselectorKind(Enum):
    """Type of connection for the UEL input used in ExcIEEEST1A.
    """
    # Ignore UEL signal.
    ignoreUELsignal = auto()
    # UEL input HV gate with voltage regulator output.
    inputHVgateVoltageOutput = auto()
    # UEL input HV gate with error signal.
    inputHVgateErrorSignal = auto()
    # UEL input added to error signal.
    inputAddedToErrorSignal = auto()