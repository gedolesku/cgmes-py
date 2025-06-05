from __future__ import annotations
from ..Core.PowerSystemResource import PowerSystemResource
from .HydroPlantStorageKind import HydroPlantStorageKind
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class HydroPowerPlant(PowerSystemResource):
    hydroPlantStorageType: HydroPlantStorageKind = field(metadata={'xpath': 'cim:HydroPowerPlant.hydroPlantStorageType'})
