from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssIEEE3B(PowerSystemStabilizerDynamics):
    """The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer
    model. The PSS model PSS3B has dual inputs of electrical power and rotor
    angular frequency deviation. The signals are used to derive an equivalent
    mechanical power signal.
    
      Reference: IEEE 3B 421.5-2005 Section 8.3.
    """
    # Type of input signal #1.  Typical Value = generatorElectricalPower.
    inputSignal1Type_: InputSignalKind  = None
 
    # Type of input signal #2.  Typical Value = rotorSpeed.
    inputSignal2Type_: InputSignalKind  = None
 
    # Transducer time constant (T1).  Typical Value = 0.012.
    t1_: Seconds  = None
 
    # Transducer time constant (T2).  Typical Value = 0.012.
    t2_: Seconds  = None
 
    # Washout time constant (Tw1).  Typical Value = 0.3.
    tw1_: Seconds  = None
 
    # Washout time constant (Tw2).  Typical Value = 0.3.
    tw2_: Seconds  = None
 
    # Washout time constant (Tw3).  Typical Value = 0.6.
    tw3_: Seconds  = None
 
    # Gain on signal # 1 (Ks1).  Typical Value = -0.602.
    ks1_: PU  = None
 
    # Gain on signal # 2 (Ks2).  Typical Value = 30.12.
    ks2_: PU  = None
 
    # Notch filter parameter (A1).  Typical Value = 0.359.
    a1_: PU  = None
 
    # Notch filter parameter (A2).  Typical Value = 0.586.
    a2_: PU  = None
 
    # Notch filter parameter (A3).  Typical Value = 0.429.
    a3_: PU  = None
 
    # Notch filter parameter (A4).  Typical Value = 0.564.
    a4_: PU  = None
 
    # Notch filter parameter (A5).  Typical Value = 0.001.
    a5_: PU  = None
 
    # Notch filter parameter (A6).  Typical Value = 0.
    a6_: PU  = None
 
    # Notch filter parameter (A7).  Typical Value = 0.031.
    a7_: PU  = None
 
    # Notch filter parameter (A8).  Typical Value = 0.
    a8_: PU  = None
 
    # Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
    vstmax_: PU  = None
 
    # Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
    vstmin_: PU  = None
     