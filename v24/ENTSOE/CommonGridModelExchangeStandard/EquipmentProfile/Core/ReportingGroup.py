from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class ReportingGroup(IdentifiedObject):
    """A reporting group is used for various ad-hoc groupings used for reporting.
    """
    pass
