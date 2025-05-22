from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Substation import Substation     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.GeographicalRegion import GeographicalRegion     

@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """A subset of a geographical region of a power system network model.
    """
    # The substations in this sub-geographical region.
    Substations: List[Substation]  = field(default_factory=list)
 
    # The geographical region to which this sub-geographical region is within.
    Region_ref: Optional[GeographicalRegion] = None
    Region: str = None
     