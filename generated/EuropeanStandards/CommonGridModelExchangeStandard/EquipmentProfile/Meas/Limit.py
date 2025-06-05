from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from typing import Protocol, runtime_checkable

@runtime_checkable
class Limit(Protocol):
    pass
