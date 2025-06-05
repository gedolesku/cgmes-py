from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from .EquipmentContainer import EquipmentContainer
from .PowerSystemResource import PowerSystemResource
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class Equipment(PowerSystemResource, Protocol):
    aggregate: Optional[Boolean]  # metadata: cim='cim:Equipment.aggregate', mult='0..1'
    EquipmentContainer_ref: Optional[EquipmentContainer]  # metadata: cim='cim:Equipment.EquipmentContainer', mult='0..1'
    EquipmentContainer_id: str
