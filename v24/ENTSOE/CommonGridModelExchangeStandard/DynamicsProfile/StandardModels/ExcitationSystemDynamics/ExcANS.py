from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcANS(ExcitationSystemDynamics):
    """Italian excitation system. It represents static field voltage or excitation
    current feedback excitation system.
    """
    # AVR gain (K<sub>3</sub>).  Typical Value = 1000.
    k3_: Simple_Float  = None
 
    # Exciter gain (K<sub>2</sub>).  Typical Value = 20.
    k2_: Simple_Float  = None
 
    # Ceiling factor (K<sub>CE</sub>).  Typical Value = 1.
    kce_: Simple_Float  = None
 
    # Time constant (T<sub>3</sub>).  Typical Value = 1.6.
    t3_: Seconds  = None
 
    # Time constant (T<sub>2</sub>).  Typical Value = 0.05.
    t2_: Seconds  = None
 
    # Time constant (T<sub>1</sub>).  Typical Value = 20.
    t1_: Seconds  = None
 
    # Governor Control Flag (BLINT).
    # 0 = lead-lag regulator
    # 1 = proportional integral regulator.
    # Typical Value = 0.
    blint_: int  = None
 
    # Rate feedback signal flag (K<sub>VFIF</sub>).
    # 0 = output voltage of the exciter
    # 1 = exciter field current.
    # Typical Value = 0.
    kvfif_: int  = None
 
    # Minimum exciter current (I<sub>FMN</sub>).  Typical Value = -5.2.
    ifmn_: PU  = None
 
    # Maximum exciter current (I<sub>FMX</sub>).  Typical Value = 6.5.
    ifmx_: PU  = None
 
    # Maximum AVR output (V<sub>RMN</sub>).  Typical Value = -5.2.
    vrmn_: PU  = None
 
    # Minimum AVR output (V<sub>RMX</sub>).  Typical Value = 6.5.
    vrmx_: PU  = None
 
    # Feedback enabling (K<sub>RVECC</sub>).
    # 0 = Open loop control
    # 1 = Closed loop control.
    # Typical Value = 1.
    krvecc_: int  = None
 
    # Exciter time constant (T<sub>B</sub>).  Typical Value = 0.04.
    tb_: Seconds  = None
     