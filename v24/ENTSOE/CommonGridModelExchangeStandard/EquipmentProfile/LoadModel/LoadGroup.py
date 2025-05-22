from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.SubLoadArea import SubLoadArea     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class LoadGroup(IdentifiedObject):
    """The class is the third level in a hierarchical structure for grouping of loads
    for the purpose of load flow load scaling.
    """
    # The SubLoadArea where the Loadgroup belongs.
    SubLoadArea_: Optional[SubLoadArea] = None
     