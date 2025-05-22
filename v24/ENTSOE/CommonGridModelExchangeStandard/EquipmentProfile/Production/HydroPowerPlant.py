from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.HydroPlantStorageKind import HydroPlantStorageKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class HydroPowerPlant(PowerSystemResource):
    """A hydro power station which can generate or pump. When generating, the
    generator turbines receive water from an upper reservoir. When pumping, the
    pumps receive their water from a lower reservoir.
    """
    # The type of hydro power plant water storage.
    hydroPlantStorageType: HydroPlantStorageKind  = None
     