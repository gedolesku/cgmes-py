from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class EquivalentEquipment(ConductingEquipment, Protocol):
    pass
