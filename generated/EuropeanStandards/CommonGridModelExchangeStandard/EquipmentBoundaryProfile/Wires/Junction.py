from __future__ import annotations
from .Connector import Connector
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Junction(Connector):
    pass
