from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAVR3(ExcitationSystemDynamics):
    """Italian excitation system. It represents exciter dynamo and electric regulator.
    """
    # AVR gain (K<sub>A</sub>).  Typical Value = 3000.
    ka_: Simple_Float  = None
 
    # Maximum AVR output (V<sub>RMN</sub>).  Typical Value = -7.5.
    vrmn_: PU  = None
 
    # Minimum AVR output (V<sub>RMX</sub>).  Typical Value = 7.5.
    vrmx_: PU  = None
 
    # AVR time constant (T<sub>1</sub>).  Typical Value = 220.
    t1_: Seconds  = None
 
    # AVR time constant (T<sub>2</sub>).  Typical Value = 1.6.
    t2_: Seconds  = None
 
    # AVR time constant (T<sub>3</sub>).  Typical Value = 0.66.
    t3_: Seconds  = None
 
    # AVR time constant (T<sub>4</sub>).  Typical Value = 0.07.
    t4_: Seconds  = None
 
    # Exciter time constant (T<sub>E</sub>).  Typical Value = 1.
    te_: Seconds  = None
 
    # Field voltage value 1 (E1).  Typical Value = 4.18.
    e1_: PU  = None
 
    # Saturation factor at E1 (S(E1)).  Typical Value = 0.1.
    se1_: Simple_Float  = None
 
    # Field voltage value 2 (E2).  Typical Value = 3.14.
    e2_: PU  = None
 
    # Saturation factor at E2 (S(E2)).  Typical Value = 0.03.
    se2_: Simple_Float  = None
     