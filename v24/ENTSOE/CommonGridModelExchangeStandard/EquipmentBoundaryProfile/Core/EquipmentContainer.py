from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.ConnectivityNodeContainer import ConnectivityNodeContainer

@dataclass
class EquipmentContainer(ConnectivityNodeContainer):
    """A modeling construct to provide a root class for containing equipment.
    """
    pass
