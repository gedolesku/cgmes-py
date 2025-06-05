from __future__ import annotations
from .GeneratingUnit import GeneratingUnit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindGeneratingUnit(GeneratingUnit):
    pass
