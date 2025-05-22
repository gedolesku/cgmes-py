from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics

@dataclass
class OverexcLim2(OverexcitationLimiterDynamics):
    """Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the
    excitation set-point by mean of non-windup integral regulator.
      Irated is the rated machine excitation current (calculated from nameplate
    conditions: V<sub>nom</sub>, P<sub>nom</sub>, CosPhi<sub>nom</sub>).
    """
    # Gain Over excitation limiter (K<sub>OI</sub>).  Typical Value = 0.1.
    koi: PU  = None
 
    # Maximum error signal (V<sub>OIMAX</sub>).  Typical Value = 0.
    voimax: PU  = None
 
    # Minimum error signal (V<sub>OIMIN</sub>).  Typical Value = -9999.
    voimin: PU  = None
 
    # Limit value of rated field current (I<sub>FDLIM</sub>).  Typical Value = 1.05.
    ifdlim: PU  = None
     