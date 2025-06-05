from __future__ import annotations
from .ACDCTerminal import ACDCTerminal
from .ConductingEquipment import ConductingEquipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class Terminal(ACDCTerminal, Protocol):
    ConductingEquipment_ref: ConductingEquipment  # metadata: cim='cim:Terminal.ConductingEquipment', mult='1'
    ConductingEquipment_id: str
