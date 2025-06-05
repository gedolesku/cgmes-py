from __future__ import annotations
from .TapChanger import TapChanger
from typing import Protocol, runtime_checkable

@runtime_checkable
class PhaseTapChanger(TapChanger, Protocol):
    pass
