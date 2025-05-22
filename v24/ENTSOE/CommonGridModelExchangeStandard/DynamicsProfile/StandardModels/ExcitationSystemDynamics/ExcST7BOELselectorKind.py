from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class ExcST7BOELselectorKind(Enum):
    """Type of connection for the OEL input used for static excitation systems type 7B.
    """
    # No OEL input is used.
    noOELinput = auto()
    # The signal is added to Vref.
    addVref = auto()
    # The signal is connected in the input of the LV gate.
    inputLVgate = auto()
    # The signal is connected in the output of the LV gate.
    outputLVgate = auto()