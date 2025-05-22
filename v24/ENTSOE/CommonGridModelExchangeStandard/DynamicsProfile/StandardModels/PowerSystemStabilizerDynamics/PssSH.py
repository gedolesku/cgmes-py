from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssSH(PowerSystemStabilizerDynamics):
    """Model for Siemens “H infinity” power system stabilizer with generator
    electrical power input.
    """
    # Main gain (K).  Typical Value = 1.
    k_: PU  = None
 
    # Gain 0 (K0).  Typical Value = 0.012.
    k0_: PU  = None
 
    # Gain 1 (K1).  Typical Value = 0.488.
    k1_: PU  = None
 
    # Gain 2 (K2).  Typical Value = 0.064.
    k2_: PU  = None
 
    # Gain 3 (K3).  Typical Value = 0.224.
    k3_: PU  = None
 
    # Gain 4 (K4).  Typical Value = 0.1.
    k4_: PU  = None
 
    # Input time constant (Td).  Typical Value = 10.
    td_: Seconds  = None
 
    # Time constant 1 (T1).  Typical Value = 0.076.
    t1_: Seconds  = None
 
    # Time constant 2 (T2).  Typical Value = 0.086.
    t2_: Seconds  = None
 
    # Time constant 3 (T3).   Typical Value = 1.068.
    t3_: Seconds  = None
 
    # Time constant 4 (T4).  Typical Value = 1.913.
    t4_: Seconds  = None
 
    # Output maximum limit (Vsmax).  Typical Value = 0.1.
    vsmax_: PU  = None
 
    # Output minimum limit (Vsmin).  Typical Value = -0.1.
    vsmin_: PU  = None
     