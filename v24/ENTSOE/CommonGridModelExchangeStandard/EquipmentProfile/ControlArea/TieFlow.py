from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Terminal import Terminal     

@dataclass
class TieFlow:
    """A flow specification in terms of location and direction for a control area.
    """
    # True if the flow into the terminal (load convention) is also flow into the
    # control area.  For example, this attribute should be true if using the tie line
    # terminal further away from the control area. For example to represent a tie to
    # a shunt component (like a load or generator) in another area, this is the near
    # end of a branch and this attribute would be specified as false.
    positiveFlowIn_: bool  = None
 
    # The terminal to which this tie flow belongs.
    Terminal_: Optional[Terminal] = None
     