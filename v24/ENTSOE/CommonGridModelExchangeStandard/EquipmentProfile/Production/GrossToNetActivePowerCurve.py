from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Curve import Curve

@dataclass
class GrossToNetActivePowerCurve(Curve):
    """Relationship between the generating unit's gross active power output on the X-
    axis (measured at the terminals of the machine(s)) and the generating unit's
    net active power output on the Y-axis (based on utility-defined measurements at
    the power station). Station service loads, when modeled, should be treated as
    non-conforming bus loads. There may be more than one curve, depending on the
    auxiliary equipment that is in service.
    """
    pass
