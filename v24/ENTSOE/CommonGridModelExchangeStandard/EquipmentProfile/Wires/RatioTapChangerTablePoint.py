from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TapChangerTablePoint import TapChangerTablePoint
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RatioTapChangerTable import RatioTapChangerTable     

@dataclass
class RatioTapChangerTablePoint(TapChangerTablePoint):
    """Describes each tap step in the ratio tap changer tabular curve.
    """
    # Points of this table.
    RatioTapChangerTable_ref: Optional[RatioTapChangerTable] = None
    RatioTapChangerTable: str = None
     