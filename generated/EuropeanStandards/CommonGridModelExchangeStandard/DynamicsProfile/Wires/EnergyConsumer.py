from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from ..StandardModels.LoadDynamics.LoadDynamics import LoadDynamics
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class EnergyConsumer(ConductingEquipment, Protocol):
    LoadDynamics_ref: Optional[LoadDynamics]  # metadata: cim='cim:EnergyConsumer.LoadDynamics', mult='0..1'
    LoadDynamics_id: str
