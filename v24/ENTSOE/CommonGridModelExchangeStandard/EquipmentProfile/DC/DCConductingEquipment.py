from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCTerminal import DCTerminal     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Equipment import Equipment

@dataclass
class DCConductingEquipment(Equipment):
    """The parts of the DC power system that are designed to carry current or that are
    conductively connected through DC terminals.
    """
    DCTerminals: List[DCTerminal]  = field(default_factory=list)
     