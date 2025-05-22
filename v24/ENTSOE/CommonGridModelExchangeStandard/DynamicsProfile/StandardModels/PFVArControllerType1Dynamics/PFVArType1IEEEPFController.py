from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics

@dataclass
class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    """The class represents IEEE PF Controller Type 1 which operates by moving the
    voltage reference directly.
    
      Reference: IEEE Standard 421.5-2005 Section 11.2.
    """
    # Overexcitation Flag (<i>OVEX</i>)
    # true = overexcited
    # false = underexcited.
    ovex_: bool  = None
 
    # PF controller time delay (<i>T</i><i><sub>PFC</sub></i>).  Typical Value = 5.
    tpfc_: Seconds  = None
 
    # Minimum machine terminal current needed to enable pf/var controller
    # (<i>V</i><i><sub>ITMIN</sub></i>).
    vitmin_: PU  = None
 
    # Synchronous machine power factor (<i>V</i><i><sub>PF</sub></i>).
    vpf_: PU  = None
 
    # PF controller dead band (<i>V</i><i><sub>PFC_BW</sub></i>).  Typical Value = 0.
    # 05.
    vpfcbw_: Simple_Float  = None
 
    # PF controller reference (<i>V</i><i><sub>PFREF</sub></i>).
    vpfref_: PU  = None
 
    # Maximum machine terminal voltage needed for pf/var controller to be enabled
    # (<i>V</i><i><sub>VTMAX</sub></i>).
    vvtmax_: PU  = None
 
    # Minimum machine terminal voltage needed to enable pf/var controller
    # (<i>V</i><i><sub>VTMIN</sub></i>).
    vvtmin_: PU  = None
     