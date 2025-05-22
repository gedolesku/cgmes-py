from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.TopologyBoundaryProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class BaseVoltage(IdentifiedObject):
    """Defines a system base voltage which is referenced.
    """
    pass
