from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.SubGeographicalRegion import SubGeographicalRegion     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class GeographicalRegion(IdentifiedObject):
    """A geographical region of a power system network model.
    """
    # All sub-geograhpical regions within this geographical region.
    Regions: List[SubGeographicalRegion]  = field(default_factory=list)
     