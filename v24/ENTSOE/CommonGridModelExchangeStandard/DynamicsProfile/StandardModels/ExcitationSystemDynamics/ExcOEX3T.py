from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcOEX3T(ExcitationSystemDynamics):
    """Modified IEEE Type ST1 Excitation System with semi-continuous and acting
    terminal voltage limiter.
    """
    # Time constant (T<sub>1</sub>).
    t1_: Seconds  = None
 
    # Time constant (T<sub>2</sub>).
    t2_: Seconds  = None
 
    # Time constant (T<sub>3</sub>).
    t3_: Seconds  = None
 
    # Time constant (T<sub>4</sub>).
    t4_: Seconds  = None
 
    # Gain (K<sub>A</sub>).
    ka_: PU  = None
 
    # Time constant (T<sub>5</sub>).
    t5_: Seconds  = None
 
    # Time constant (T<sub>6</sub>).
    t6_: Seconds  = None
 
    # Limiter (V<sub>RMAX</sub>).
    vrmax_: PU  = None
 
    # Limiter (V<sub>RMIN</sub>). 
    vrmin_: PU  = None
 
    # Time constant (T<sub>E</sub>).
    te_: Seconds  = None
 
    # Gain (K<sub>F</sub>).
    kf_: PU  = None
 
    # Time constant (T<sub>F</sub>).
    tf_: Seconds  = None
 
    # Gain (K<sub>C</sub>).
    kc_: PU  = None
 
    # Gain (K<sub>D</sub>).
    kd_: PU  = None
 
    # Gain (K<sub>E</sub>).
    ke_: PU  = None
 
    # Saturation parameter (E<sub>1</sub>).
    e1_: PU  = None
 
    # Saturation parameter (S<sub>E</sub>(E<sub>1</sub>)).
    see1_: PU  = None
 
    # Saturation parameter (E<sub>2</sub>).
    e2_: PU  = None
 
    # Saturation parameter (S<sub>E</sub>(E<sub>2</sub>)).
    see2_: PU  = None
     