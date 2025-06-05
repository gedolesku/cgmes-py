from __future__ import annotations
from .ConnectivityNodeContainer import ConnectivityNodeContainer
from typing import Protocol, runtime_checkable

@runtime_checkable
class EquipmentContainer(ConnectivityNodeContainer, Protocol):
    pass
