from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEST2A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems
    utilize both current and voltage sources (generator terminal quantities) to
    comprise the power source.  The regulator controls the exciter output through
    controlled saturation of the power transformer components.  These compound-
    source rectifier excitation systems are designated Type ST2A and are
    represented by ExcIEEEST2A.
    
      Reference: IEEE Standard 421.5-2005 Section 7.2.
    """
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 120.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.15.
    ta_: Seconds  = None
 
    # Maximum voltage regulator outputs (V<sub>RMAX</sub>).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (V<sub>RMIN</sub>).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 0.5.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
    # 05.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 1.
    tf_: Seconds  = None
 
    # Potential circuit gain coefficient (K<sub>P</sub>).  Typical Value = 4.88.
    kp_: PU  = None
 
    # Potential circuit gain coefficient (K<sub>I</sub>).  Typical Value = 8.
    ki_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 1.82.
    kc_: PU  = None
 
    # Maximum field voltage (E<sub>FDMax</sub>).  Typical Value = 99.
    efdmax_: PU  = None
 
    # UEL input (UELin).
    # true = HV gate
    # false = add to error signal.
    # Typical Value = true.
    uelin_: bool  = None
     