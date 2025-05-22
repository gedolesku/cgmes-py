from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PhaseCode import PhaseCode     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ACDCTerminal import ACDCTerminal
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConnectivityNode import ConnectivityNode     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment     

@dataclass
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment. Terminals
    are connected at physical connection points called connectivity nodes.
    """
    # Represents the normal network phasing condition.
    # If the attribute is missing three phases (ABC or ABCN) shall be assumed.
    phases: PhaseCode  = None
 
    # Terminals interconnected with zero impedance at a this connectivity node. 
    ConnectivityNode_ref: Optional[ConnectivityNode] = None
    ConnectivityNode: str = None
 
    # The conducting equipment of the terminal.  Conducting equipment have  terminals
    # that may be connected to other conducting equipment terminals via connectivity
    # nodes or topological nodes.
    ConductingEquipment_ref: Optional[ConductingEquipment] = None
    ConductingEquipment: str = None
     