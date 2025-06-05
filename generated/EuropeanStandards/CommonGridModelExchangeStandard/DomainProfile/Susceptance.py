from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Susceptance:
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:Susceptance.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:Susceptance.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:Susceptance.value'})
