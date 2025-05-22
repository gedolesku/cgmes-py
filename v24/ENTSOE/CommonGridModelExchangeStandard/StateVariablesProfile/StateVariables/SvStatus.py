from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.ConductingEquipment import ConductingEquipment     

@dataclass
class SvStatus:
    """State variable for status.
    """
    # The in service status as a result of topology processing.
    inService: bool  = None
 
    # The conducting equipment associated with the status state variable.
    ConductingEquipment_ref: Optional[ConductingEquipment] = None
    ConductingEquipment: str = None
     