from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class ExcST6BOELselectorKind(Enum):
    """Type of connection for the OEL input used for static excitation systems type 6B.
    """
    # No OEL input is used.
    noOELinput = auto()
    # The connection is before UEL.
    beforeUEL = auto()
    # The connection is after UEL.
    afterUEL = auto()