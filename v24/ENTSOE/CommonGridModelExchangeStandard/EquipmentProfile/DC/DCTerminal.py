from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCBaseTerminal import DCBaseTerminal
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment     

@dataclass
class DCTerminal(DCBaseTerminal):
    """An electrical connection point to generic DC conducting equipment.
    """
    DCConductingEquipment_ref: Optional[DCConductingEquipment] = None
    DCConductingEquipment: str = None
     