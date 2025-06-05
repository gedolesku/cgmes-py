from __future__ import annotations
from .Float import Float
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Simple_Float:
    value: Float = field(metadata={'xpath': 'cim:Simple_Float.value'})
