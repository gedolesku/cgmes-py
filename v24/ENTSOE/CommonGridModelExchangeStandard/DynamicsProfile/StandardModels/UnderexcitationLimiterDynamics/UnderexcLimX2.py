from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics

@dataclass
class UnderexcLimX2(UnderexcitationLimiterDynamics):
    """<font color="#0f0f0f">Westinghouse minimum excitation limiter.</font>
    """
    # Differential gain (Kf2).
    kf2_: PU  = None
 
    # Differential time constant (Tf2) (>0).
    tf2_: Seconds  = None
 
    # Minimum excitation limit gain (Km).
    km_: PU  = None
 
    # Minimum excitation limit time constant (Tm).
    tm_: Seconds  = None
 
    # Minimum excitation limit value (MELMAX).
    melmax_: PU  = None
 
    # Excitation center setting (Qo).
    qo_: PU  = None
 
    # Excitation radius (R).
    r_: PU  = None
     