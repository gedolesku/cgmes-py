from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TapChangerTablePoint import TapChangerTablePoint
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChangerTable import PhaseTapChangerTable     

@dataclass
class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """Describes each tap step in the phase tap changer tabular curve.
    """
    # The angle difference in degrees.
    angle: AngleDegrees  = None
 
    # The table of this point.
    PhaseTapChangerTable_ref: Optional[PhaseTapChangerTable] = None
    PhaseTapChangerTable: str = None
     