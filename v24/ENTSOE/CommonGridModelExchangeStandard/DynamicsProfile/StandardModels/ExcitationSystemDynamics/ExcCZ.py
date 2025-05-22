from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcCZ(ExcitationSystemDynamics):
    """Czech Proportion/Integral Exciter.
    """
    # Regulator proportional gain (Kp).
    kp_: PU  = None
 
    # Regulator integral time constant (Tc). 
    tc_: Seconds  = None
 
    # Voltage regulator maximum limit (Vrmax). 
    vrmax_: PU  = None
 
    # Voltage regulator minimum limit (Vrmin). 
    vrmin_: PU  = None
 
    # Regulator gain (Ka).
    ka_: PU  = None
 
    # Regulator time constant (Ta).
    ta_: Seconds  = None
 
    # Exciter constant related to self-excited field (Ke).
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    te_: Seconds  = None
 
    # Exciter output maximum limit (Efdmax).
    efdmax_: PU  = None
 
    # Exciter output minimum limit (Efdmin). 
    efdmin_: PU  = None
     