from __future__ import annotations
from .RotatingMachine import RotatingMachine
from typing import Protocol, runtime_checkable

@runtime_checkable
class AsynchronousMachine(RotatingMachine, Protocol):
    pass
