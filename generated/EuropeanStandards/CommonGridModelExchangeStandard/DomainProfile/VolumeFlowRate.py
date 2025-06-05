from __future__ import annotations
from .Float import Float
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class VolumeFlowRate:
    denominatorMultiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:VolumeFlowRate.denominatorMultiplier'})
    denominatorUnit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:VolumeFlowRate.denominatorUnit'})
    multiplier: Optional[UnitMultiplier] = field(default=None, metadata={'xpath': 'cim:VolumeFlowRate.multiplier'})
    unit: Optional[UnitSymbol] = field(default=None, metadata={'xpath': 'cim:VolumeFlowRate.unit'})
    value: Optional[Float] = field(default=None, metadata={'xpath': 'cim:VolumeFlowRate.value'})
