from __future__ import annotations
from .LimitTypeKind import LimitTypeKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ENTSOEOperationalLimitType:
    limitType: Optional[LimitTypeKind] = field(default=None, metadata={'xpath': 'cim:ENTSOEOperationalLimitType.limitType'})
