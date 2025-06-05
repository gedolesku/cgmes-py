from __future__ import annotations
from .Switch import Switch
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Disconnector(Switch):
    pass
