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
    kp: PU  = None
 
    # Regulator integral time constant (Tc). 
    tc: Seconds  = None
 
    # Voltage regulator maximum limit (Vrmax). 
    vrmax: PU  = None
 
    # Voltage regulator minimum limit (Vrmin). 
    vrmin: PU  = None
 
    # Regulator gain (Ka).
    ka: PU  = None
 
    # Regulator time constant (Ta).
    ta: Seconds  = None
 
    # Exciter constant related to self-excited field (Ke).
    ke: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    te: Seconds  = None
 
    # Exciter output maximum limit (Efdmax).
    efdmax: PU  = None
 
    # Exciter output minimum limit (Efdmin). 
    efdmin: PU  = None
     