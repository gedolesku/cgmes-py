from __future__ import annotations
from .ACDCTerminal import ACDCTerminal
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Terminal(ACDCTerminal):
    pass
