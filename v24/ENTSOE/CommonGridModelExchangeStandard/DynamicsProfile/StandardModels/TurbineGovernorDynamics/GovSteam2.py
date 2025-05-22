from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteam2(TurbineGovernorDynamics):
    """Simplified governor model.
    """
    # Governor gain (reciprocal of droop) (K).  Typical Value = 20.
    k_: Simple_Float  = None
 
    # Frequency dead band (DBF).  Typical Value = 0.
    dbf_: PU  = None
 
    # Governor lag time constant (T<sub>1</sub>) (>0).  Typical Value = 0.45.
    t1_: Seconds  = None
 
    # Governor lead time constant (T<sub>2</sub>) (may be 0).  Typical Value = 0.
    t2_: Seconds  = None
 
    # Maximum fuel flow (P<sub>MAX</sub>).  Typical Value = 1.
    pmax_: PU  = None
 
    # Minimum fuel flow (P<sub>MIN</sub>).  Typical Value = 0.
    pmin_: PU  = None
 
    # Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 1.
    mxef_: PU  = None
 
    # Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -1.
    mnef_: PU  = None
     