from __future__ import annotations
from .GeneratingUnit import GeneratingUnit
from .WindGenUnitKind import WindGenUnitKind
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindGeneratingUnit(GeneratingUnit):
    windGenUnitType: WindGenUnitKind = field(metadata={'xpath': 'cim:WindGeneratingUnit.windGenUnitType'})
