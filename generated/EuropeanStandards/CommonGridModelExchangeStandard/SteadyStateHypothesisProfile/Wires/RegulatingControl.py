from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Simple_Float import Simple_Float
from ...DomainProfile.UnitMultiplier import UnitMultiplier
from ..Core.PowerSystemResource import PowerSystemResource
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class RegulatingControl(PowerSystemResource):
    discrete: Boolean = field(metadata={'xpath': 'cim:RegulatingControl.discrete'})
    enabled: Boolean = field(metadata={'xpath': 'cim:RegulatingControl.enabled'})
    targetValue: Simple_Float = field(metadata={'xpath': 'cim:RegulatingControl.targetValue'})
    targetValueUnitMultiplier: UnitMultiplier = field(metadata={'xpath': 'cim:RegulatingControl.targetValueUnitMultiplier'})
    targetDeadband: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:RegulatingControl.targetDeadband'})
