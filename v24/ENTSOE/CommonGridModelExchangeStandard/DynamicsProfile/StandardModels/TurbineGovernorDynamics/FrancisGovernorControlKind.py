from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class FrancisGovernorControlKind(Enum):
    """Governor control flag for Francis hydro model.
    """
    # Mechanic-hydraulic regulator with tacho-accelerometer (Cflag = 1).
    mechanicHydrolicTachoAccelerator = auto()
    # Mechanic-hydraulic regulator with transient feedback (Cflag=2).
    mechanicHydraulicTransientFeedback = auto()
    # Electromechanical and electrohydraulic regulator (Cflag=3).
    electromechanicalElectrohydraulic = auto()