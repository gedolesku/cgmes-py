from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics

@dataclass
class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    """The class represents IEEE VAR Controller Type 1 which operates by moving the
    voltage reference directly.
    
      Reference: IEEE Standard 421.5-2005 Section 11.3.
    """
    # Var controller time delay (<i>T</i><i><sub>VARC</sub></i>).  Typical Value = 5.
    tvarc_: Seconds  = None
 
    # Synchronous machine power factor (<i>V</i><i><sub>VAR</sub></i>).
    vvar_: PU  = None
 
    # Var controller dead band (<i>V</i><i><sub>VARC_BW</sub></i>).  Typical Value =
    # 0.02.
    vvarcbw_: Simple_Float  = None
 
    # Var controller reference (<i>V</i><i><sub>VARREF</sub></i>).
    vvarref_: PU  = None
 
    # Maximum machine terminal voltage needed for pf/var controller to be enabled
    # (<i>V</i><i><sub>VTMAX</sub></i>).
    vvtmax_: PU  = None
 
    # Minimum machine terminal voltage needed to enable pf/var controller
    # (<i>V</i><i><sub>VTMIN</sub></i>).
    vvtmin_: PU  = None
     