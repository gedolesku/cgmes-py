from __future__ import annotations
from .Equipment import Equipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class ConductingEquipment(Equipment, Protocol):
    pass
