from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """A base class for all objects that may contain connectivity nodes or topological
    nodes.
    """
    pass
