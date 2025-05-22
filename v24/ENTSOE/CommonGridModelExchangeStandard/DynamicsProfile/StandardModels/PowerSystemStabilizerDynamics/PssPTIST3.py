from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
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
    m_: PU  = None
 
    # Time constant (Tf).  Typical Value = 0.2.
    tf_: Seconds  = None
 
    # Time constant (Tp).  Typical Value = 0.2.
    tp_: Seconds  = None
 
    # Time constant (T1).  Typical Value = 0.3.
    t1_: Seconds  = None
 
    # Time constant (T2).  Typical Value = 1.
    t2_: Seconds  = None
 
    # Time constant (T3).  Typical Value = 0.2.
    t3_: Seconds  = None
 
    # Time constant (T4).  Typical Value = 0.05.
    t4_: Seconds  = None
 
    # Gain (K).  Typical Value = 9.
    k_: PU  = None
 
    # Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025.
    dtf_: Seconds  = None
 
    # Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical
    # Value = 0.025.
    dtc_: Seconds  = None
 
    # Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.
    # 0125.
    dtp_: Seconds  = None
 
    # Time constant (T5). 
    t5_: Seconds  = None
 
    # Time constant (T6). 
    t6_: Seconds  = None
 
    # Filter coefficient (A0). 
    a0_: PU  = None
 
    # Limiter (Al). 
    a1_: PU  = None
 
    # Filter coefficient (A2). 
    a2_: PU  = None
 
    # Filter coefficient (B0). 
    b0_: PU  = None
 
    # Filter coefficient (B1). 
    b1_: PU  = None
 
    # Filter coefficient (B2). 
    b2_: PU  = None
 
    # Filter coefficient (A3). 
    a3_: PU  = None
 
    # Filter coefficient (A4). 
    a4_: PU  = None
 
    # Filter coefficient (A5). 
    a5_: PU  = None
 
    # Filter coefficient (B3). 
    b3_: PU  = None
 
    # Filter coefficient (B4). 
    b4_: PU  = None
 
    # Filter coefficient (B5). 
    b5_: PU  = None
 
    # Threshold value above which output averaging will be bypassed (Athres).
    # Typical Value = 0.005.
    athres_: PU  = None
 
    # Limiter (Dl). 
    dl_: PU  = None
 
    # Limiter (Al).
    al_: PU  = None
 
    # Threshold value (Lthres).
    lthres_: PU  = None
 
    # (Pmin).
    pmin_: PU  = None
 
    # Digital/analog output switch (Isw).
    # true = produce analog output
    # false = convert to digital output, using tap selection table. 
    isw_: bool  = None
 
    # Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4.
    nav_: Simple_Float  = None
 
    # Number of counts at limit to active limit function (Ncl) (>0). 
    ncl_: Simple_Float  = None
 
    # Number of counts until reset after limit function is triggered (Ncr). 
    ncr_: Simple_Float  = None
     