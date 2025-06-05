from __future__ import annotations
from .DCBaseTerminal import DCBaseTerminal
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCTerminal(DCBaseTerminal):
    pass
