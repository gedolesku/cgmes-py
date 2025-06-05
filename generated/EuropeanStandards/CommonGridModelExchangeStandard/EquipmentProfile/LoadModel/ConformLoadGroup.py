from __future__ import annotations
from .LoadGroup import LoadGroup
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ConformLoadGroup(LoadGroup):
    pass
