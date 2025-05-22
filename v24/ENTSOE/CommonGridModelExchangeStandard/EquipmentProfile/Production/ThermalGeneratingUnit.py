from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratingUnit import GeneratingUnit

@dataclass
class ThermalGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover could be a steam turbine, combustion
    turbine, or diesel engine.
    """
    pass
