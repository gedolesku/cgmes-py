from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssPTIST3(PowerSystemStabilizerDynamics):
    """PTI Microprocessor-Based Stabilizer type 3.
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
 
    # Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025.
    dtf: Seconds  = None
 
    # Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical
    # Value = 0.025.
    dtc: Seconds  = None
 
    # Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.
    # 0125.
    dtp: Seconds  = None
 
    # Time constant (T5). 
    t5: Seconds  = None
 
    # Time constant (T6). 
    t6: Seconds  = None
 
    # Filter coefficient (A0). 
    a0: PU  = None
 
    # Limiter (Al). 
    a1: PU  = None
 
    # Filter coefficient (A2). 
    a2: PU  = None
 
    # Filter coefficient (B0). 
    b0: PU  = None
 
    # Filter coefficient (B1). 
    b1: PU  = None
 
    # Filter coefficient (B2). 
    b2: PU  = None
 
    # Filter coefficient (A3). 
    a3: PU  = None
 
    # Filter coefficient (A4). 
    a4: PU  = None
 
    # Filter coefficient (A5). 
    a5: PU  = None
 
    # Filter coefficient (B3). 
    b3: PU  = None
 
    # Filter coefficient (B4). 
    b4: PU  = None
 
    # Filter coefficient (B5). 
    b5: PU  = None
 
    # Threshold value above which output averaging will be bypassed (Athres).
    # Typical Value = 0.005.
    athres: PU  = None
 
    # Limiter (Dl). 
    dl: PU  = None
 
    # Limiter (Al).
    al: PU  = None
 
    # Threshold value (Lthres).
    lthres: PU  = None
 
    # (Pmin).
    pmin: PU  = None
 
    # Digital/analog output switch (Isw).
    # true = produce analog output
    # false = convert to digital output, using tap selection table. 
    isw: bool  = None
 
    # Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4.
    nav: Simple_Float  = None
 
    # Number of counts at limit to active limit function (Ncl) (>0). 
    ncl: Simple_Float  = None
 
    # Number of counts until reset after limit function is triggered (Ncr). 
    ncr: Simple_Float  = None
     