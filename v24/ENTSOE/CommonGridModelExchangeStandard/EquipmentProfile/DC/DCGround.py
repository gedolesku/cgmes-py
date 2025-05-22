from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Inductance import Inductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCGround(DCConductingEquipment):
    """A ground within a DC system.
    """
    # Inductance to ground.
    inductance_: Inductance  = None
 
    # Resistance to ground.
    r_: Resistance  = None
     