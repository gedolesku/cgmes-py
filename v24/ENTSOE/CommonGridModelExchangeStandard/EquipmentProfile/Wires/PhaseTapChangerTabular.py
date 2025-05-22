from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChanger import PhaseTapChanger
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChangerTable import PhaseTapChangerTable     

@dataclass
class PhaseTapChangerTabular(PhaseTapChanger):
    # The phase tap changer table for this phase tap changer.
    PhaseTapChangerTable_: Optional[PhaseTapChangerTable] = None
     