from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from .IdentifiedObject import IdentifiedObject
from typing import Protocol, runtime_checkable

@runtime_checkable
class ACDCTerminal(Protocol):
    connected: Boolean  # metadata: cim='cim:ACDCTerminal.connected', mult='1'
