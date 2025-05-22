from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssIEEE1A(PowerSystemStabilizerDynamics):
    """The class represents IEEE Std 421.5-2005 type PSS1A power system stabilizer
    model. PSS1A is the generalized form of a PSS with a single input. Some common
    stabilizer input signals are speed, frequency, and power.
    
      Reference: IEEE 1A 421.5-2005 Section 8.1.
    """
    # Type of input signal.  Typical Value = rotorAngularFrequencyDeviation.
    inputSignalType_: InputSignalKind  = None
 
    # PSS signal conditioning frequency filter constant (A1).  Typical Value = 0.061.
    a1_: PU  = None
 
    # PSS signal conditioning frequency filter constant (A2).  Typical Value = 0.0017.
    a2_: PU  = None
 
    # Lead/lag time constant (T1).  Typical Value = 0.3.
    t1_: Seconds  = None
 
    # Lead/lag time constant (T2).  Typical Value = 0.03.
    t2_: Seconds  = None
 
    # Lead/lag time constant (T3).  Typical Value = 0.3.
    t3_: Seconds  = None
 
    # Lead/lag time constant (T4).  Typical Value = 0.03.
    t4_: Seconds  = None
 
    # Washout time constant (T5).  Typical Value = 10.
    t5_: Seconds  = None
 
    # Transducer time constant (T6).  Typical Value = 0.01.
    t6_: Seconds  = None
 
    # Stabilizer gain (Ks).  Typical Value = 5.
    ks_: PU  = None
 
    # Maximum stabilizer output (Vrmax).  Typical Value = 0.05.
    vrmax_: PU  = None
 
    # Minimum stabilizer output (Vrmin).  Typical Value = -0.05.
    vrmin_: PU  = None
     