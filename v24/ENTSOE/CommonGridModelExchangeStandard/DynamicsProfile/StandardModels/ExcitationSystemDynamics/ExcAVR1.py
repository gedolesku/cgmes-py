from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAVR1(ExcitationSystemDynamics):
    """Italian excitation system corresponding to IEEE (1968) Type 1 Model. It
    represents exciter dynamo and electromechanical regulator.
    """
    # AVR gain (K<sub>A</sub>).  Typical Value = 500.
    ka_: Simple_Float  = None
 
    # Maximum AVR output (V<sub>RMN</sub>).  Typical Value = -6.
    vrmn_: PU  = None
 
    # Minimum AVR output (V<sub>RMX</sub>).  Typical Value = 7.
    vrmx_: PU  = None
 
    # AVR time constant (T<sub>A</sub>).  Typical Value = 0.2.
    ta_: Seconds  = None
 
    # AVR time constant (T<sub>B</sub>).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Exciter time constant (T<sub>E</sub>).  Typical Value = 1.
    te_: Seconds  = None
 
    # Field voltage value 1  (E1).  Typical Value = 4.18.
    e1_: PU  = None
 
    # Saturation factor at E1 (S(E1)).  Typical Value = 0.1.
    se1_: Simple_Float  = None
 
    # Field voltage value 2 (E2).  Typical Value = 3.14.
    e2_: PU  = None
 
    # Saturation factor at E2 (S(E2)).  Typical Value = 0.03.
    se2_: Simple_Float  = None
 
    # Rate feedback gain (K<sub>F</sub>).  Typical Value = 0.02.
    kf_: Simple_Float  = None
 
    # Rate feedback time constant (T<sub>F</sub>).  Typical Value = 1.
    tf_: Seconds  = None
     