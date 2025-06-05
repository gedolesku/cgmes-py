from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ..Topology.BusNameMarker import BusNameMarker
from .IdentifiedObject import IdentifiedObject
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class ACDCTerminal(Protocol):
    sequenceNumber: Optional[Integer]  # metadata: cim='cim:ACDCTerminal.sequenceNumber', mult='0..1'
    BusNameMarker_ref: Optional[BusNameMarker]  # metadata: cim='cim:ACDCTerminal.BusNameMarker', mult='0..1'
    BusNameMarker_id: str
