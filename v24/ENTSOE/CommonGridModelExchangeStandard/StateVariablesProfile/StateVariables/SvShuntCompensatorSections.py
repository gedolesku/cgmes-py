from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Wires.ShuntCompensator import ShuntCompensator     

@dataclass
class SvShuntCompensatorSections:
    """State variable for the number of sections in service for a shunt compensator.
    """
    # The number of sections in service as a continous variable. To get integer value
    # scale with ShuntCompensator.bPerSection.
    sections_: Simple_Float  = None
 
    # The shunt compensator for which the state applies.
    ShuntCompensator_: Optional[ShuntCompensator] = None
     