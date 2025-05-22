from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.ACDCTerminal import ACDCTerminal
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.ConductingEquipment import ConductingEquipment     

@dataclass
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment. Terminals
    are connected at physical connection points called connectivity nodes.
    """
    # The conducting equipment of the terminal.  Conducting equipment have  terminals
    # that may be connected to other conducting equipment terminals via connectivity
    # nodes or topological nodes.
    ConductingEquipment_ref: Optional[ConductingEquipment] = None
    ConductingEquipment: str = None
     