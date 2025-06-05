from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class CapacitancePerLength:
    denominatorMultiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:CapacitancePerLength.denominatorMultiplier'})
    denominatorUnit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:CapacitancePerLength.denominatorUnit'})
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:CapacitancePerLength.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:CapacitancePerLength.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:CapacitancePerLength.value'})
