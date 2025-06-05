from __future__ import annotations
from ..Core.Equipment import Equipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class DCConductingEquipment(Equipment, Protocol):
    pass
