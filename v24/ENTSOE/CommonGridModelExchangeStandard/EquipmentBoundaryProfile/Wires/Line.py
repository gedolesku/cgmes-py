from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.EquipmentContainer import EquipmentContainer

@dataclass
class Line(EquipmentContainer):
    """Contains equipment beyond a substation belonging to a power transmission line.
    """
    pass
