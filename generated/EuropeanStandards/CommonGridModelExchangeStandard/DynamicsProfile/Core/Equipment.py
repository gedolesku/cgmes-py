from __future__ import annotations
from .PowerSystemResource import PowerSystemResource
from typing import Protocol, runtime_checkable

@runtime_checkable
class Equipment(PowerSystemResource, Protocol):
    pass
