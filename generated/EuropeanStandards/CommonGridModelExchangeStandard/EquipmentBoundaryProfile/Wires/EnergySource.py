from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from .EnergySchedulingType import EnergySchedulingType
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class EnergySource(ConductingEquipment, Protocol):
    EnergySchedulingType_ref: Optional[EnergySchedulingType]  # metadata: cim='cim:EnergySource.EnergySchedulingType', mult='0..1'
    EnergySchedulingType_id: str
