from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class PhaseTapChangerTable(IdentifiedObject):
    """Describes a tabular curve for how the phase angle difference and impedance
    varies with the tap step.
    """
    pass
