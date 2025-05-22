from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssSK(PowerSystemStabilizerDynamics):
    """PSS Slovakian type � three inputs.
    """
    # Gain P (K1).  Typical Value = -0.3.
    k1_: PU  = None
 
    # Gain fe (K2).  Typical Value = -0.15.
    k2_: PU  = None
 
    # Gain If (K3).  Typical Value = 10.
    k3_: PU  = None
 
    # Denominator time constant (T1).  Typical Value = 0.3.
    t1_: Seconds  = None
 
    # Filter time constant (T2).  Typical Value = 0.35.
    t2_: Seconds  = None
 
    # Denominator time constant (T3).  Typical Value = 0.22.
    t3_: Seconds  = None
 
    # Filter time constant (T4).  Typical Value = 0.02.
    t4_: Seconds  = None
 
    # Denominator time constant (T5).  Typical Value = 0.02.
    t5_: Seconds  = None
 
    # Filter time constant (T6).  Typical Value = 0.02.
    t6_: Seconds  = None
 
    # Stabilizer output max limit (Vsmax).  Typical Value = 0.4.
    vsmax_: PU  = None
 
    # Stabilizer output min limit (Vsmin).  Typical Value = -0.4.
    vsmin_: PU  = None
     