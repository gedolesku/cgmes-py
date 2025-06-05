from __future__ import annotations
from .Currency import Currency
from .Decimal import Decimal
from .UnitMultiplier import UnitMultiplier
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Money:
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:Money.multiplier'})
    unit: Optional[Currency] = field(default=None, metadata={'xpath': 'cim:Money.unit'})
    value: Optional[Decimal] = field(default=None, metadata={'xpath': 'cim:Money.value'})
