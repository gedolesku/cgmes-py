from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.Terminal import Terminal     

@dataclass
class SvPowerFlow:
    """State variable for power flow. Load convention is used for flow direction. This
    means flow out from the TopologicalNode into the equipment is positive.
    """
    # The active power flow. Load sign convention is used, i.e. positive sign means
    # flow out from a TopologicalNode (bus) into the conducting equipment.
    p_: ActivePower  = None
 
    # The reactive power flow. Load sign convention is used, i.e. positive sign means
    # flow out from a TopologicalNode (bus) into the conducting equipment.
    q_: ReactivePower  = None
 
    # The terminal associated with the power flow state variable.
    Terminal_: Optional[Terminal] = None
     