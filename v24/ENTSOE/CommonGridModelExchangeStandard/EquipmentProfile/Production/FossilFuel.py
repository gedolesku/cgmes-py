from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.FuelType import FuelType     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.ThermalGeneratingUnit import ThermalGeneratingUnit     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating unit.   For
    example, coal, oil, gas, etc.   This a the specific fuels that the generating
    unit can consume.
    """
    # The type of fossil fuel, such as coal, oil, or gas.
    fossilFuelType_: FuelType  = None
 
    # A thermal generating unit may have one or more fossil fuels.
    ThermalGeneratingUnit_: Optional[ThermalGeneratingUnit] = None
     