from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.DateTime import DateTime
from ...DomainProfile.String import String
from ...DomainProfile.UnitMultiplier import UnitMultiplier
from ...DomainProfile.UnitSymbol import UnitSymbol
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.PowerSystemResource import PowerSystemResource
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class Control(Protocol):
    controlType: String  # metadata: cim='cim:Control.controlType', mult='1'
    operationInProgress: Optional[Boolean]  # metadata: cim='cim:Control.operationInProgress', mult='0..1'
    timeStamp: Optional[DateTime]  # metadata: cim='cim:Control.timeStamp', mult='0..1'
    unitMultiplier: Optional[UnitMultiplier]  # metadata: cim='cim:Control.unitMultiplier', mult='0..1'
    unitSymbol: Optional[UnitSymbol]  # metadata: cim='cim:Control.unitSymbol', mult='0..1'
    PowerSystemResource_ref: Optional[PowerSystemResource]  # metadata: cim='cim:Control.PowerSystemResource', mult='0..1'
    PowerSystemResource_id: str
