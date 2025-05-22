from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.TopologyProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class ACDCTerminal(IdentifiedObject):
    """An electrical connection point (AC or DC) to a piece of conducting equipment.
    Terminals are connected at physical connection points called connectivity nodes.
    """
    pass
