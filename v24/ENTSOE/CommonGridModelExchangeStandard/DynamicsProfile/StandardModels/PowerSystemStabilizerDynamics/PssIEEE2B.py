from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssIEEE2B(PowerSystemStabilizerDynamics):
    """The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer
    model. This stabilizer model is designed to represent a variety of dual-input
    stabilizers, which normally use combinations of power and speed or frequency to
    derive the stabilizing signal.
    
      Reference: IEEE 2B 421.5-2005 Section 8.2.
    """
    # Type of input signal #1.  Typical Value = rotorSpeed.
    inputSignal1Type_: InputSignalKind  = None
 
    # Type of input signal #2.  Typical Value = generatorElectricalPower.
    inputSignal2Type_: InputSignalKind  = None
 
    # Input signal #1 max limit (Vsi1max).  Typical Value = 2.
    vsi1max_: PU  = None
 
    # Input signal #1 min limit (Vsi1min).  Typical Value = -2.
    vsi1min_: PU  = None
 
    # First washout on signal #1 (Tw1).  Typical Value = 2.
    tw1_: Seconds  = None
 
    # Second washout on signal #1 (Tw2).  Typical Value = 2.
    tw2_: Seconds  = None
 
    # Input signal #2 max limit (Vsi2max).  Typical Value = 2.
    vsi2max_: PU  = None
 
    # Input signal #2 min limit (Vsi2min).  Typical Value = -2.
    vsi2min_: PU  = None
 
    # First washout on signal #2 (Tw3).  Typical Value = 2.
    tw3_: Seconds  = None
 
    # Second washout on signal #2 (Tw4).  Typical Value = 0.
    tw4_: Seconds  = None
 
    # Lead/lag time constant (T1).  Typical Value = 0.12.
    t1_: Seconds  = None
 
    # Lead/lag time constant (T2).  Typical Value = 0.02.
    t2_: Seconds  = None
 
    # Lead/lag time constant (T3).  Typical Value = 0.3.
    t3_: Seconds  = None
 
    # Lead/lag time constant (T4).  Typical Value = 0.02.
    t4_: Seconds  = None
 
    # Time constant on signal #1 (T6).  Typical Value = 0.
    t6_: Seconds  = None
 
    # Time constant on signal #2 (T7).  Typical Value = 2.
    t7_: Seconds  = None
 
    # Lead of ramp tracking filter (T8).  Typical Value = 0.2.
    t8_: Seconds  = None
 
    # Lag of ramp tracking filter (T9).  Typical Value = 0.1.
    t9_: Seconds  = None
 
    # Lead/lag time constant (T10).  Typical Value = 0.
    t10_: Seconds  = None
 
    # Lead/lag time constant (T11).  Typical Value = 0.
    t11_: Seconds  = None
 
    # Stabilizer gain (Ks1).  Typical Value = 12.
    ks1_: PU  = None
 
    # Gain on signal #2 (Ks2).  Typical Value = 0.2.
    ks2_: PU  = None
 
    # Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1.
    ks3_: PU  = None
 
    # Order of ramp tracking filter (N).  Typical Value = 1.
    n_: int  = None
 
    # Denominator order of ramp tracking filter (M).  Typical Value = 5.
    m_: int  = None
 
    # Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
    vstmax_: PU  = None
 
    # Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
    vstmin_: PU  = None
     