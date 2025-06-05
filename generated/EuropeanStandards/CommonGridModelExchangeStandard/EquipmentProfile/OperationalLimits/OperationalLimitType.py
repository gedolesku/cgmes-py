from __future__ import annotations
from ...DomainProfile.Seconds import Seconds
from ..Core.IdentifiedObject import IdentifiedObject
from .LimitTypeKind import LimitTypeKind
from .OperationalLimitDirectionKind import OperationalLimitDirectionKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class OperationalLimitType(IdentifiedObject):
    limitType: LimitTypeKind = field(metadata={'xpath': 'cim:OperationalLimitType.limitType'})
    acceptableDuration: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:OperationalLimitType.acceptableDuration'})
    direction: Optional[OperationalLimitDirectionKind] = field(default=None, metadata={'xpath': 'cim:OperationalLimitType.direction'})
