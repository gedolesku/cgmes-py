from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.HydroEnergyConversionKind import HydroEnergyConversionKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.HydroPowerPlant import HydroPowerPlant     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratingUnit import GeneratingUnit

@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover is a hydraulic turbine (e.g., Francis,
    Pelton, Kaplan).
    """
    # Energy conversion capability for generating.
    energyConversionCapability_: HydroEnergyConversionKind  = None
 
    # The hydro generating unit belongs to a hydro power plant.
    HydroPowerPlant_: Optional[HydroPowerPlant] = None
     