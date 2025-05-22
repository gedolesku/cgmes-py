from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class RatioTapChangerTable(IdentifiedObject):
    """Describes a curve for how the voltage magnitude and impedance varies with the
    tap step.
    """
    pass
