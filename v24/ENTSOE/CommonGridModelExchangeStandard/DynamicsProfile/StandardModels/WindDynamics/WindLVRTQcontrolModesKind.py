from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class WindLVRTQcontrolModesKind(Enum):
    """LVRT Q control modes <i>M</i><sub>qLVRT</sub>.
    """
    # Voltage dependent reactive current injection (<i>M</i><sub>LVRT,1</sub>).
    mode1 = auto()
    # Reactive current injection controlled as the pre-fault value plus an additional
    # voltage dependent reactive current injection (<i>M</i><sub>LVRT,2</sub>).
    mode2 = auto()
    # Reactive current injection controlled as the pre-fault value plus an additional
    # voltage dependent reactive current injection during fault, and as the pre-fault
    # value plus an additional constant reactive current injection post fault
    # (<i>M</i><sub>LVRT,3</sub>).
    mode3 = auto()