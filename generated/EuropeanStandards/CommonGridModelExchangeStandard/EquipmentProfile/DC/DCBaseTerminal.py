from __future__ import annotations
from ..Core.ACDCTerminal import ACDCTerminal
from .DCNode import DCNode
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class DCBaseTerminal(ACDCTerminal, Protocol):
    DCNode_ref: Optional[DCNode]  # metadata: cim='cim:DCBaseTerminal.DCNode', mult='0..1'
    DCNode_id: str
