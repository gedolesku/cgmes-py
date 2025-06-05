from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class RegulatingCondEq(ConductingEquipment, Protocol):
    controlEnabled: Boolean  # metadata: cim='cim:RegulatingCondEq.controlEnabled', mult='1'
