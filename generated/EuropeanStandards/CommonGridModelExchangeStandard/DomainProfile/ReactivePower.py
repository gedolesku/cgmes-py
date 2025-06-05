from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ReactivePower:
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:ReactivePower.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:ReactivePower.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:ReactivePower.value'})
