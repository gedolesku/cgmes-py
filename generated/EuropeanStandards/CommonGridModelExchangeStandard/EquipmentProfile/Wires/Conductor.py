from __future__ import annotations
from ...DomainProfile.Length import Length
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class Conductor(ConductingEquipment, Protocol):
    length: Optional[Length]  # metadata: cim='cim:Conductor.length', mult='0..1'
