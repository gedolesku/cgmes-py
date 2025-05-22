from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingControl import RegulatingControl     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class RegulatingCondEq(ConductingEquipment):
    """A type of conducting equipment that can regulate a quantity (i.e. voltage or
    flow) at a specific point in the network.
    """
    # The regulating control scheme in which this equipment participates.
    RegulatingControl_: Optional[RegulatingControl] = None
     