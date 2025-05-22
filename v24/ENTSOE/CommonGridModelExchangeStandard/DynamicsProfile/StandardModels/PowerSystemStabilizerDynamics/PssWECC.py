from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssWECC(PowerSystemStabilizerDynamics):
    """Dual input Power System Stabilizer, based on IEEE type 2, with modified output
    limiter defined by WECC (Western Electricity Coordinating Council, USA).
    """
    # Type of input signal #1.
    inputSignal1Type_: InputSignalKind  = None
 
    # Type of input signal #2.
    inputSignal2Type_: InputSignalKind  = None
 
    # Input signal 1 gain  (K<sub>1</sub>). 
    k1_: PU  = None
 
    # Input signal 1 transducer time constant (T<sub>1</sub>).
    t1_: Seconds  = None
 
    # Input signal 2 gain (K<sub>2</sub>). 
    k2_: PU  = None
 
    # Input signal 2 transducer time constant (T<sub>2</sub>). 
    t2_: Seconds  = None
 
    # Stabilizer washout time constant (T<sub>3</sub>). 
    t3_: Seconds  = None
 
    # Stabilizer washout time lag constant (T<sub>4</sub>) (>0).
    t4_: Seconds  = None
 
    # Lead time constant (T<sub>5</sub>). 
    t5_: Seconds  = None
 
    # Lag time constant (T<sub>6</sub>). 
    t6_: Seconds  = None
 
    # Lead time constant (T<sub>7</sub>). 
    t7_: Seconds  = None
 
    # Lag time constant (T<sub>8</sub>). 
    t8_: Seconds  = None
 
    # Lag time constant (T<sub>10</sub>). 
    t10_: Seconds  = None
 
    # Lead time constant (T<sub>9</sub>). 
    t9_: Seconds  = None
 
    # Maximum output signal (Vsmax). 
    vsmax_: PU  = None
 
    # Minimum output signal (Vsmin). 
    vsmin_: PU  = None
 
    # Maximum value for voltage compensator output (V<sub>CU</sub>). 
    vcu_: PU  = None
 
    # Minimum value for voltage compensator output (V<sub>CL</sub>). 
    vcl_: PU  = None
     