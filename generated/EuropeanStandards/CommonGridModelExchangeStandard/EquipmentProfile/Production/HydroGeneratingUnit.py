from __future__ import annotations
from .GeneratingUnit import GeneratingUnit
from .HydroEnergyConversionKind import HydroEnergyConversionKind
from .HydroPowerPlant import HydroPowerPlant
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class HydroGeneratingUnit(GeneratingUnit):
    energyConversionCapability: Optional[HydroEnergyConversionKind] = field(default=None, metadata={'xpath': 'cim:HydroGeneratingUnit.energyConversionCapability'})
    HydroPowerPlant_id: str | None = field(default=None, metadata={"xpath": "cim:HydroGeneratingUnit.HydroPowerPlant/@rdf:resource", "pattern": r"^#.+$"})
    HydroPowerPlant_ref: HydroPowerPlant | None = None
