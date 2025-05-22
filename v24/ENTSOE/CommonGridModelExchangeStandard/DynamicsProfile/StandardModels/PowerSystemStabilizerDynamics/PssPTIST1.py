from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssPTIST1(PowerSystemStabilizerDynamics):
    """PTI Microprocessor-Based Stabilizer type 1.
    """
    # (M).  M=2*H.  Typical Value = 5.
    m: PU  = None
 
    # Time constant (Tf).  Typical Value = 0.2.
    tf: Seconds  = None
 
    # Time constant (Tp).  Typical Value = 0.2.
    tp: Seconds  = None
 
    # Time constant (T1).  Typical Value = 0.3.
    t1: Seconds  = None
 
    # Time constant (T2).  Typical Value = 1.
    t2: Seconds  = None
 
    # Time constant (T3).  Typical Value = 0.2.
    t3: Seconds  = None
 
    # Time constant (T4).  Typical Value = 0.05.
    t4: Seconds  = None
 
    # Gain (K).  Typical Value = 9.
    k: PU  = None
 
    # Time step frequency calculation (Dtf).  Typical Value = 0.025.
    dtf: Seconds  = None
 
    # Time step related to activation of controls (Dtc).  Typical Value = 0.025.
    dtc: Seconds  = None
 
    # Time step active power calculation (Dtp).  Typical Value = 0.0125.
    dtp: Seconds  = None
     