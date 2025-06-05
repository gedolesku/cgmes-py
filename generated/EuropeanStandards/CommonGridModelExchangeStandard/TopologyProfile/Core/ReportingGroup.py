from __future__ import annotations
from .IdentifiedObject import IdentifiedObject
from typing import Protocol, runtime_checkable

@runtime_checkable
class ReportingGroup(Protocol):
    pass
