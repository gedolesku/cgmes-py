from __future__ import annotations
from ...DomainProfile.Voltage import Voltage
from .BaseVoltage import BaseVoltage
from .EquipmentContainer import EquipmentContainer
from .Substation import Substation
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class VoltageLevel(EquipmentContainer):
    BaseVoltage_id: str | None = field(default=None, metadata={"xpath": "cim:VoltageLevel.BaseVoltage/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    BaseVoltage_ref: BaseVoltage = None
    Substation_id: str | None = field(default=None, metadata={"xpath": "cim:VoltageLevel.Substation/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Substation_ref: Substation = None
    highVoltageLimit: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:VoltageLevel.highVoltageLimit'})
    lowVoltageLimit: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:VoltageLevel.lowVoltageLimit'})
