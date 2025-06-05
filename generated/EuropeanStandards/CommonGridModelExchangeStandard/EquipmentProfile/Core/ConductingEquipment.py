from __future__ import annotations
from .BaseVoltage import BaseVoltage
from .Equipment import Equipment
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class ConductingEquipment(Equipment, Protocol):
    BaseVoltage_ref: Optional[BaseVoltage]  # metadata: cim='cim:ConductingEquipment.BaseVoltage', mult='0..1'
    BaseVoltage_id: str
