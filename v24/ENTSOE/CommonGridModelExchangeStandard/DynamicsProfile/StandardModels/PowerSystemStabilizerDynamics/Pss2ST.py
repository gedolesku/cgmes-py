from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class Pss2ST(PowerSystemStabilizerDynamics):
    """PTI Microprocessor-Based Stabilizer type 1.
    """
    # Type of input signal #1.  Typical Value = rotorAngularFrequencyDeviation.
    inputSignal1Type_: InputSignalKind  = None
 
    # Type of input signal #2.  Typical Value = generatorElectricalPower.
    inputSignal2Type_: InputSignalKind  = None
 
    # Gain (K1). 
    k1_: PU  = None
 
    # Gain (K2). 
    k2_: PU  = None
 
    # Time constant (T1). 
    t1_: Seconds  = None
 
    # Time constant (T2).
    t2_: Seconds  = None
 
    # Time constant (T3). 
    t3_: Seconds  = None
 
    # Time constant (T4).
    t4_: Seconds  = None
 
    # Time constant (T5). 
    t5_: Seconds  = None
 
    # Time constant (T6). 
    t6_: Seconds  = None
 
    # Time constant (T7). 
    t7_: Seconds  = None
 
    # Time constant (T8). 
    t8_: Seconds  = None
 
    # Time constant (T9). 
    t9_: Seconds  = None
 
    # Time constant (T10). 
    t10_: Seconds  = None
 
    # Limiter (Lsmax). 
    lsmax_: PU  = None
 
    # Limiter (Lsmin). 
    lsmin_: PU  = None
 
    # Cutoff limiter (Vcu). 
    vcu_: PU  = None
 
    # Cutoff limiter (Vcl). 
    vcl_: PU  = None
     