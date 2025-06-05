from __future__ import annotations
from ..Core.ACDCTerminal import ACDCTerminal
from .DCTopologicalNode import DCTopologicalNode
from typing import Protocol, runtime_checkable

@runtime_checkable
class DCBaseTerminal(ACDCTerminal, Protocol):
    DCTopologicalNode_ref: DCTopologicalNode  # metadata: cim='cim:DCBaseTerminal.DCTopologicalNode', mult='1'
    DCTopologicalNode_id: str
