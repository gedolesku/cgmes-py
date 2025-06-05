from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..Core.IdentifiedObject import IdentifiedObject
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class LimitSet(Protocol):
    isPercentageLimits: Optional[Boolean]  # metadata: cim='cim:LimitSet.isPercentageLimits', mult='0..1'
