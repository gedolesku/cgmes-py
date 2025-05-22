from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DCTopologicalNode(IdentifiedObject):
    """DC bus.
    """
    pass
