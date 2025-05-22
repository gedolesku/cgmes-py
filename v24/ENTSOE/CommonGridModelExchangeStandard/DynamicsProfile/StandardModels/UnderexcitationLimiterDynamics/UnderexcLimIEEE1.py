from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics

@dataclass
class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """The class represents the Type UEL1 model which has a circular limit boundary
    when plotted in terms of machine reactive power vs. real power output.
    
      Reference: IEEE UEL1 421.5-2005 Section 10.1.
    """
    # UEL radius setting (K<sub>UR</sub>).  Typical Value = 1.95.
    kur: PU  = None
 
    # UEL center setting (K<sub>UC</sub>).  Typical Value = 1.38.
    kuc: PU  = None
 
    # UEL excitation system stabilizer gain (K<sub>UF</sub>).  Typical Value = 3.3.
    kuf: PU  = None
 
    # UEL maximum limit for radius phasor magnitude (V<sub>URMAX</sub>).  Typical
    # Value = 5.8.
    vurmax: PU  = None
 
    # UEL maximum limit for operating point phasor magnitude (V<sub>UCMAX</sub>).
    # Typical Value = 5.8.
    vucmax: PU  = None
 
    # UEL integral gain (K<sub>UI</sub>).  Typical Value = 0.
    kui: PU  = None
 
    # UEL proportional gain (K<sub>UL</sub>).  Typical Value = 100.
    kul: PU  = None
 
    # UEL integrator output maximum limit (V<sub>UIMAX</sub>).
    vuimax: PU  = None
 
    # UEL integrator output minimum limit (V<sub>UIMIN</sub>).
    vuimin: PU  = None
 
    # UEL lead time constant (T<sub>U1</sub>).  Typical Value = 0.
    tu1: Seconds  = None
 
    # UEL lag time constant (T<sub>U2</sub>).  Typical Value = 0.05.
    tu2: Seconds  = None
 
    # UEL lead time constant (T<sub>U3</sub>).  Typical Value = 0.
    tu3: Seconds  = None
 
    # UEL lag time constant (T<sub>U4</sub>).  Typical Value = 0.
    tu4: Seconds  = None
 
    # UEL output maximum limit (V<sub>ULMAX</sub>).  Typical Value = 18.
    vulmax: PU  = None
 
    # UEL output minimum limit (V<sub>ULMIN</sub>).  Typical Value = -18.
    vulmin: PU  = None
     