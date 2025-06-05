from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Capacitance:
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:Capacitance.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:Capacitance.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:Capacitance.value'})
