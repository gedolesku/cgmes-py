from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class WindQcontrolModesKind(Enum):
    """General wind turbine Q control modes <i>M</i><sub>qG</sub>.
    """
    # Voltage control (<i>M</i><sub>G,u</sub>).
    voltage = auto()
    # Reactive power control (<i>M</i><sub>G,q</sub>).
    reactivePower = auto()
    # Open loop reactive power control (only used with closed loop at plant level)
    # (<i>M</i><sub>G,qol</sub>).
    openLoopReactivePower = auto()
    # Power factor control (<i>M</i><sub>G,pf</sub>).
    powerFactor = auto()