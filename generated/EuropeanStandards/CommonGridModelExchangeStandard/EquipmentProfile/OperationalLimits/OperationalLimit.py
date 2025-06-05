from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .OperationalLimitSet import OperationalLimitSet
from .OperationalLimitType import OperationalLimitType
from typing import Protocol, runtime_checkable

@runtime_checkable
class OperationalLimit(Protocol):
    OperationalLimitType_ref: OperationalLimitType  # metadata: cim='cim:OperationalLimit.OperationalLimitType', mult='1'
    OperationalLimitType_id: str
    OperationalLimitSet_ref: OperationalLimitSet  # metadata: cim='cim:OperationalLimit.OperationalLimitSet', mult='1'
    OperationalLimitSet_id: str
