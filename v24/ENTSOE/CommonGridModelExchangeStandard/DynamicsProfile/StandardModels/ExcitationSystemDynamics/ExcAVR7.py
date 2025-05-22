from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAVR7(ExcitationSystemDynamics):
    """IVO excitation system.
    """
    # Gain (K1).  Typical Value = 1.
    k1_: PU  = None
 
    # Lead coefficient (A1).  Typical Value = 0.5.
    a1_: PU  = None
 
    # Lag coefficient (A2).  Typical Value = 0.5.
    a2_: PU  = None
 
    # Lead time constant (T1).  Typical Value = 0.05.
    t1_: Seconds  = None
 
    # Lag time constant (T2).  Typical Value = 0.1.
    t2_: Seconds  = None
 
    # Lead-lag max. limit (Vmax1).  Typical Value = 5.
    vmax1_: PU  = None
 
    # Lead-lag min. limit (Vmin1).  Typical Value = -5.
    vmin1_: PU  = None
 
    # Gain (K3).  Typical Value = 3.
    k3_: PU  = None
 
    # Lead coefficient (A3).  Typical Value = 0.5.
    a3_: PU  = None
 
    # Lag coefficient (A4).  Typical Value = 0.5.
    a4_: PU  = None
 
    # Lead time constant (T3).  Typical Value = 0.1.
    t3_: Seconds  = None
 
    # Lag time constant (T4).  Typical Value = 0.1.
    t4_: Seconds  = None
 
    # Lead-lag max. limit (Vmax3).  Typical Value = 5.
    vmax3_: PU  = None
 
    # Lead-lag min. limit (Vmin3).  Typical Value = -5.
    vmin3_: PU  = None
 
    # Gain (K5).  Typical Value = 1.
    k5_: PU  = None
 
    # Lead coefficient (A5).  Typical Value = 0.5.
    a5_: PU  = None
 
    # Lag coefficient (A6).  Typical Value = 0.5.
    a6_: PU  = None
 
    # Lead time constant (T5).  Typical Value = 0.1.
    t5_: Seconds  = None
 
    # Lag time constant (T6).  Typical Value = 0.1.
    t6_: Seconds  = None
 
    # Lead-lag max. limit (Vmax5).  Typical Value = 5.
    vmax5_: PU  = None
 
    # Lead-lag min. limit (Vmin5).  Typical Value = -2.
    vmin5_: PU  = None
     