from __future__ import annotations
from .RegulatingCondEq import RegulatingCondEq
from typing import Protocol, runtime_checkable

@runtime_checkable
class RotatingMachine(RegulatingCondEq, Protocol):
    pass
