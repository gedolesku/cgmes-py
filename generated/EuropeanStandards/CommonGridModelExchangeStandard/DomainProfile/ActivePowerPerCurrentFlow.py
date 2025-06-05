from __future__ import annotations
from .UnitMultiplier import UnitMultiplier
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ActivePowerPerCurrentFlow:
    denominatorMultiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:ActivePowerPerCurrentFlow.denominatorMultiplier'})
    denominatorUnit: Optional[str] = field(default=None, metadata={'xpath': 'cim:ActivePowerPerCurrentFlow.denominatorUnit'})
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:ActivePowerPerCurrentFlow.multiplier'})
    unit: Optional[str] = field(default=None, metadata={'xpath': 'cim:ActivePowerPerCurrentFlow.unit'})
    value: Optional[str] = field(default=None, metadata={'xpath': 'cim:ActivePowerPerCurrentFlow.value'})
