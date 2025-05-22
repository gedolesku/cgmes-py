from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    t1: Seconds  = None
 
    # Time constant (T<sub>2</sub>).
    t2: Seconds  = None
 
    # Time constant (T<sub>3</sub>).
    t3: Seconds  = None
 
    # Time constant (T<sub>4</sub>).
    t4: Seconds  = None
 
    # Gain (K<sub>A</sub>).
    ka: PU  = None
 
    # Time constant (T<sub>5</sub>).
    t5: Seconds  = None
 
    # Time constant (T<sub>6</sub>).
    t6: Seconds  = None
 
    # Limiter (V<sub>RMAX</sub>).
    vrmax: PU  = None
 
    # Limiter (V<sub>RMIN</sub>). 
    vrmin: PU  = None
 
    # Time constant (T<sub>E</sub>).
    te: Seconds  = None
 
    # Gain (K<sub>F</sub>).
    kf: PU  = None
 
    # Time constant (T<sub>F</sub>).
    tf: Seconds  = None
 
    # Gain (K<sub>C</sub>).
    kc: PU  = None
 
    # Gain (K<sub>D</sub>).
    kd: PU  = None
 
    # Gain (K<sub>E</sub>).
    ke: PU  = None
 
    # Saturation parameter (E<sub>1</sub>).
    e1: PU  = None
 
    # Saturation parameter (S<sub>E</sub>(E<sub>1</sub>)).
    see1: PU  = None
 
    # Saturation parameter (E<sub>2</sub>).
    e2: PU  = None
 
    # Saturation parameter (S<sub>E</sub>(E<sub>2</sub>)).
    see2: PU  = None
     