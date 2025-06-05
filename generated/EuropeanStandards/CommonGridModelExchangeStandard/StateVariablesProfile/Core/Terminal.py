from __future__ import annotations
from .ACDCTerminal import ACDCTerminal
from typing import Protocol, runtime_checkable

@runtime_checkable
class Terminal(ACDCTerminal, Protocol):
    pass
