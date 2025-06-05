from __future__ import annotations
from .DCSwitch import DCSwitch
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCBreaker(DCSwitch):
    pass
