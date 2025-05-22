from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class ExcST7BUELselectorKind(Enum):
    """Type of connection for the UEL input used for static excitation systems type 7B.
    """
    # No UEL input is used.
    noUELinput = auto()
    # The signal is added to Vref.
    addVref = auto()
    # The signal is connected in the input of the HV gate.
    inputHVgate = auto()
    # The signal is connected in the output of the HV gate.
    outputHVgate = auto()