from __future__ import annotations
from ...DomainProfile.DateTime import DateTime
from ...DomainProfile.UnitSymbol import UnitSymbol
from .IdentifiedObject import IdentifiedObject
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class BasicIntervalSchedule(Protocol):
    startTime: DateTime  # metadata: cim='cim:BasicIntervalSchedule.startTime', mult='1'
    value1Unit: UnitSymbol  # metadata: cim='cim:BasicIntervalSchedule.value1Unit', mult='1'
    value2Unit: Optional[UnitSymbol]  # metadata: cim='cim:BasicIntervalSchedule.value2Unit', mult='0..1'
