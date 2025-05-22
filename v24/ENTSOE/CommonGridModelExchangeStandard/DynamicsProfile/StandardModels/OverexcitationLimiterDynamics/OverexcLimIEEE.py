from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics

@dataclass
class OverexcLimIEEE(OverexcitationLimiterDynamics):
    """The over excitation limiter model is intended to represent the significant
    features of OELs necessary for some large-scale system studies. It is the
    result of a pragmatic approach to obtain a model that can be widely applied
    with attainable data from generator owners. An attempt to include all
    variations in the functionality of OELs and duplicate how they interact with
    the rest of the excitation systems would likely result in a level of
    application insufficient for the studies for which they are intended.
    
      Reference: IEEE OEL 421.5-2005 Section 9.
    """
    # OEL timed field current limiter pickup level (I<sub>TFPU</sub>).  Typical Value
    # = 1.05.
    itfpu_: PU  = None
 
    # OEL instantaneous field current limit (I<sub>FDMAX</sub>).  Typical Value = 1.5.
    ifdmax_: PU  = None
 
    # OEL timed field current limit (I<sub>FDLIM</sub>).  Typical Value = 1.05.
    ifdlim_: PU  = None
 
    # OEL pickup/drop-out hysteresis (HYST).  Typical Value = 0.03.
    hyst_: PU  = None
 
    # OEL cooldown gain (K<sub>CD</sub>).  Typical Value = 1.
    kcd_: PU  = None
 
    # OEL ramped limit rate (K<sub>RAMP</sub>).  Unit = PU/sec.  Typical Value = 10.
    kramp_: Simple_Float  = None
     