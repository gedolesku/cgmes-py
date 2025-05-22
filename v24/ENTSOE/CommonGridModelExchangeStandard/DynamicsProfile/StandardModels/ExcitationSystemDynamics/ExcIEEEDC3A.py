from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEDC3A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type DC3A model. This model represents
    represent older systems, in particular those dc commutator exciters with non-
    continuously acting regulators that were commonly used before the development
    of the continuously acting varieties.  These systems respond at basically two
    different rates, depending upon the magnitude of voltage error. For small
    errors, adjustment is made periodically with a signal to a motor-operated
    rheostat. Larger errors cause resistors to be quickly shorted or inserted and a
    strong forcing signal applied to the exciter. Continuous motion of the motor-
    operated rheostat occurs for these larger error signals, even though it is
    bypassed by contactor action.
    
    
      Reference: IEEE Standard 421.5-2005 Section 5.3.
    """
    # Rheostat travel time (T<sub>RH</sub>).  Typical Value = 20.
    trh_: Seconds  = None
 
    # Fast raise/lower contact setting (K<sub>V</sub>).  Typical Value = 0.05.
    kv_: PU  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 0.5.
    te_: Seconds  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 0.05.
    ke_: PU  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
    # Typical Value = 3.375.
    efd1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.267.
    seefd1_: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
    # Typical Value = 3.15.
    efd2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.068.
    seefd2_: Simple_Float  = None
 
    # (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
    # true = a lower limit of zero is applied to integrator output
    # false = a lower limit of zero is not applied to integrator output.
    # Typical Value = true.
    exclim_: bool  = None
     