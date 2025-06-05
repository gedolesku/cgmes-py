from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .FuelType import FuelType
from .ThermalGeneratingUnit import ThermalGeneratingUnit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class FossilFuel(IdentifiedObject):
    fossilFuelType: FuelType = field(metadata={'xpath': 'cim:FossilFuel.fossilFuelType'})
    ThermalGeneratingUnit_id: str | None = field(default=None, metadata={"xpath": "cim:FossilFuel.ThermalGeneratingUnit/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ThermalGeneratingUnit_ref: ThermalGeneratingUnit = None
