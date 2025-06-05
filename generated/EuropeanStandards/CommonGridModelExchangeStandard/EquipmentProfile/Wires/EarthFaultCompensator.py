from __future__ import annotations
from ...DomainProfile.Resistance import Resistance
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class EarthFaultCompensator(ConductingEquipment, Protocol):
    r: Optional[Resistance]  # metadata: cim='cim:EarthFaultCompensator.r', mult='0..1'
