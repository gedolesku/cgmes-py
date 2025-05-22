from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Topology.BusNameMarker import BusNameMarker     

@dataclass
class ACDCTerminal(IdentifiedObject):
    """An electrical connection point (AC or DC) to a piece of conducting equipment.
    Terminals are connected at physical connection points called connectivity nodes.
    """
    # The orientation of the terminal connections for a multiple terminal conducting
    # equipment.  The sequence numbering starts with 1 and additional terminals
    # should follow in increasing order.   The first terminal is the "starting point"
    # for a two terminal branch.
    sequenceNumber: int  = None
 
    # The bus name marker used to name the bus (topological node).
    BusNameMarker_ref: Optional[BusNameMarker] = None
    BusNameMarker: str = None
     