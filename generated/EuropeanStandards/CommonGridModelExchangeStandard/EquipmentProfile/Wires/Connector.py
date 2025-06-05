from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class Connector(ConductingEquipment, Protocol):
    pass
