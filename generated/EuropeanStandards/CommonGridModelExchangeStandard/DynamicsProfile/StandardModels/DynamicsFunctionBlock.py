from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..Core.IdentifiedObject import IdentifiedObject
from typing import Protocol, runtime_checkable

@runtime_checkable
class DynamicsFunctionBlock(Protocol):
    enabled: Boolean  # metadata: cim='cim:DynamicsFunctionBlock.enabled', mult='1'
