from __future__ import annotations
from ..Core.ConductingEquipment import ConductingEquipment
from .RegulatingControl import RegulatingControl
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class RegulatingCondEq(ConductingEquipment, Protocol):
    RegulatingControl_ref: Optional[RegulatingControl]  # metadata: cim='cim:RegulatingCondEq.RegulatingControl', mult='0..1'
    RegulatingControl_id: str
