from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PFVArControllerType2Dynamics.PFVArControllerType2Dynamics import PFVArControllerType2Dynamics

@dataclass
class PFVArType2IEEEVArController(PFVArControllerType2Dynamics):
    """The class represents IEEE VAR Controller Type 2 which is a summing point type
    controller. It makes up the outside loop of a two-loop system. This controller
    is implemented as a slow PI type controller, and the voltage regulator forms
    the inner loop and is implemented as a fast controller.
    
      Reference: IEEE Standard 421.5-2005 Section 11.5.
    """
    # Reactive power reference (<i>Q</i><i><sub>REF</sub></i>). 
    qref: PU  = None
 
    # Voltage regulator reference (<i>V</i><i><sub>REF</sub></i>).
    vref: PU  = None
 
    # Maximum output of the pf controller (<i>V</i><i><sub>CLMT</sub></i>).
    vclmt: PU  = None
 
    # Proportional gain of the pf controller (<i>K</i><i><sub>P</sub></i>).
    kp: PU  = None
 
    # Integral gain of the pf controller (<i>K</i><i><sub>I</sub></i>).
    ki: PU  = None
 
    # Generator sensing voltage (<i>V</i><i><sub>S</sub></i>).
    vs: Simple_Float  = None
 
    # Overexcitation or under excitation flag (<i>EXLON</i>)
    # true = 1 (not in the overexcitation or underexcitation state, integral action
    # is active)
    # false = 0 (in the overexcitation or underexcitation state, so integral action
    # is disabled to allow the limiter to play its role).
    exlon: bool  = None
     