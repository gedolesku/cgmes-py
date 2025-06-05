from __future__ import annotations
from .ProtectedSwitch import ProtectedSwitch
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Breaker(ProtectedSwitch):
    pass
