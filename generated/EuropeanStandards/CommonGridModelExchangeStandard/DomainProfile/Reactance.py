from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Reactance:
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:Reactance.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:Reactance.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:Reactance.value'})
