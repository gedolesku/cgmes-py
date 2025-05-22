from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class Pss1A(PowerSystemStabilizerDynamics):
    """Single input power system stabilizer. It is a modified version in order to
    allow representation of various vendors' implementations on PSS type 1A.
    """
    # Type of input signal.
    inputSignalType_: InputSignalKind  = None
 
    # Notch filter parameter (A1).
    a1_: PU  = None
 
    # Notch filter parameter (A2). 
    a2_: PU  = None
 
    # Lead/lag time constant (T1). 
    t1_: Seconds  = None
 
    # Lead/lag time constant (T2). 
    t2_: Seconds  = None
 
    # Lead/lag time constant (T3). 
    t3_: Seconds  = None
 
    # Lead/lag time constant (T4). 
    t4_: Seconds  = None
 
    # Washout time constant (T5). 
    t5_: Seconds  = None
 
    # Transducer time constant (T6). 
    t6_: Seconds  = None
 
    # Stabilizer gain (Ks). 
    ks_: PU  = None
 
    # Maximum stabilizer output (Vrmax). 
    vrmax_: PU  = None
 
    # Minimum stabilizer output (Vrmin). 
    vrmin_: PU  = None
 
    # Stabilizer input cutoff threshold (Vcu). 
    vcu_: PU  = None
 
    # Stabilizer input cutoff threshold (Vcl). 
    vcl_: PU  = None
 
    # Notch filter parameter (A3). 
    a3_: PU  = None
 
    # Notch filter parameter (A4). 
    a4_: PU  = None
 
    # Notch filter parameter (A5). 
    a5_: PU  = None
 
    # Notch filter parameter (A6). 
    a6_: PU  = None
 
    # Notch filter parameter (A7). 
    a7_: PU  = None
 
    # Notch filter parameter (A8). 
    a8_: PU  = None
 
    # Selector (Kd).
    # true = e<sup>-sTdelay</sup> used
    # false = e<sup>-sTdelay</sup> not used.
    kd_: bool  = None
 
    # Time constant (Tdelay). 
    tdelay_: Seconds  = None
     