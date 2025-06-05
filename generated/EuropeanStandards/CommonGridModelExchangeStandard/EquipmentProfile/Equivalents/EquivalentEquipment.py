from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from .EquivalentNetwork import EquivalentNetwork
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class EquivalentEquipment(ConductingEquipment, Protocol):
    EquivalentNetwork_ref: Optional[EquivalentNetwork]  # metadata: cim='cim:EquivalentEquipment.EquivalentNetwork', mult='0..1'
    EquivalentNetwork_id: str
