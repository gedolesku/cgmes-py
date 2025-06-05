from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ResistancePerLength:
    denominatorMultiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:ResistancePerLength.denominatorMultiplier'})
    denominatorUnit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:ResistancePerLength.denominatorUnit'})
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:ResistancePerLength.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:ResistancePerLength.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:ResistancePerLength.value'})
