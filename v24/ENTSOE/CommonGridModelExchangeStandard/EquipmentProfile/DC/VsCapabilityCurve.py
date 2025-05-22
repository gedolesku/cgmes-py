from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Curve import Curve

@dataclass
class VsCapabilityCurve(Curve):
    """The P-Q capability curve for a voltage source converter, with P on x-axis and
    Qmin and Qmax on y1-axis and y2-axis.
    """
    pass
