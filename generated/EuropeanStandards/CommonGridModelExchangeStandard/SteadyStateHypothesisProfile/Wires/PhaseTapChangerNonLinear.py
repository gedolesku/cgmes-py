from __future__ import annotations
from .PhaseTapChanger import PhaseTapChanger
from typing import Protocol, runtime_checkable

@runtime_checkable
class PhaseTapChangerNonLinear(PhaseTapChanger, Protocol):
    pass
