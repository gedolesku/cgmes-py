from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from .SubLoadArea import SubLoadArea
from typing import Protocol, runtime_checkable

@runtime_checkable
class LoadGroup(Protocol):
    SubLoadArea_ref: SubLoadArea  # metadata: cim='cim:LoadGroup.SubLoadArea', mult='1'
    SubLoadArea_id: str
