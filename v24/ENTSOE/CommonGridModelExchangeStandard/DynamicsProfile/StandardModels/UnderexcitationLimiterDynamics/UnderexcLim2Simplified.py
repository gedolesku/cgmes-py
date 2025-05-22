from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics

@dataclass
class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    """This model can be derived from UnderexcLimIEEE2.
      The limit characteristic (look –up table) is a single straight-line, the same
    as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).
    """
    # Segment Q initial point (Q0).  Typical Value = -0.31.
    q0_: PU  = None
 
    # Segment Q end point (Q1).  Typical Value = -0.1.
    q1_: PU  = None
 
    # Segment P initial point (P0).  Typical Value = 0.
    p0_: PU  = None
 
    # Segment P end point (P1).  Typical Value = 1.
    p1_: PU  = None
 
    # Gain Under excitation limiter (Kui).  Typical Value = 0.1.
    kui_: PU  = None
 
    # Minimum error signal (V<sub>UImin</sub>).  Typical Value = 0.
    vuimin_: PU  = None
 
    # Maximum error signal (V<sub>UImax</sub>).  Typical Value = 1.
    vuimax_: PU  = None
     