from __future__ import annotations
from ..Core.ACDCTerminal import ACDCTerminal
from typing import Protocol, runtime_checkable

@runtime_checkable
class DCBaseTerminal(ACDCTerminal, Protocol):
    pass
