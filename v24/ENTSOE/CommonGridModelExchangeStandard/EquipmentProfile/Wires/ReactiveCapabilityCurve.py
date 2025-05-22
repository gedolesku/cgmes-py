from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Curve import Curve

@dataclass
class ReactiveCapabilityCurve(Curve):
    """Reactive power rating envelope versus the synchronous machine's active power,
    in both the generating and motoring modes. For each active power value there is
    a corresponding high and low reactive power limit  value. Typically there will
    be a separate curve for each coolant condition, such as hydrogen pressure.  The
    Y1 axis values represent reactive minimum and the Y2 axis values represent
    reactive maximum.
    """
    pass
