from __future__ import annotations
from .Switch import Switch
from typing import Protocol, runtime_checkable

@runtime_checkable
class ProtectedSwitch(Protocol):
    pass
