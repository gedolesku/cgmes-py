from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.WindGenUnitKind import WindGenUnitKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratingUnit import GeneratingUnit

@dataclass
class WindGeneratingUnit(GeneratingUnit):
    """A wind driven generating unit.  May be used to represent a single turbine or an
    aggregation.
    """
    # The kind of wind generating unit
    windGenUnitType: WindGenUnitKind  = None
     