from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAVR4(ExcitationSystemDynamics):
    """Italian excitation system. It represents static exciter and electric voltage
    regulator.
    """
    # AVR gain (K<sub>A</sub>).  Typical Value = 300.
    ka_: Simple_Float  = None
 
    # Maximum AVR output (V<sub>RMN</sub>).  Typical Value = 0.
    vrmn_: PU  = None
 
    # Minimum AVR output (V<sub>RMX</sub>).  Typical Value = 5.
    vrmx_: PU  = None
 
    # AVR time constant (T<sub>1</sub>).  Typical Value = 4.8.
    t1_: Seconds  = None
 
    # AVR time constant (T<sub>2</sub>).  Typical Value = 1.5.
    t2_: Seconds  = None
 
    # AVR time constant (T<sub>3</sub>).  Typical Value = 0.
    t3_: Seconds  = None
 
    # AVR time constant (T<sub>4</sub>).  Typical Value = 0.
    t4_: Seconds  = None
 
    # Exciter gain (K<sub>E</sub>).  Typical Value = 1.
    ke_: Simple_Float  = None
 
    # Maximum exciter output (V<sub>FMX</sub>).  Typical Value = 5.
    vfmx_: PU  = None
 
    # Minimum exciter output (V<sub>FMN</sub>).  Typical Value = 0.
    vfmn_: PU  = None
 
    # Exciter internal reactance (K<sub>IF</sub>).  Typical Value = 0.
    kif_: Simple_Float  = None
 
    # Exciter current feedback time constant (T<sub>IF</sub>).  Typical Value = 0.
    tif_: Seconds  = None
 
    # Exciter current feedback time constant (T<sub>1IF</sub>).  Typical Value = 60.
    t1if_: Seconds  = None
 
    # AVR output voltage dependency selector (Imul).
    # true = selector is connected
    # false = selector is not connected.
    # Typical Value = true.
    imul_: bool  = None
     