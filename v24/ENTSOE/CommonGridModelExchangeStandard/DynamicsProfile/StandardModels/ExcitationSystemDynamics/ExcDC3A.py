from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcDC3A(ExcitationSystemDynamics):
    """This is modified IEEE DC3A direct current commutator exciters with speed input,
    and death band.  DC old type 4.
    """
    # Rheostat travel time (Trh).  Typical Value = 20.
    trh_: Seconds  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Death band (Kr).  If Kr is not zero, the voltage regulator input changes at a
    # constant rate if Verr > Kr or Verr < -Kr as per the IEEE (1968) Type 4 model.
    # If Kr is zero, the error signal drives the voltage regulator continuously as
    # per the IEEE (1980) DC3 and IEEE (1992, 2005) DC3A models.  Typical Value = 0.
    kr_: PU  = None
 
    # Fast raise/lower contact setting (Kv).  Typical Value = 0.05.
    kv_: PU  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 5.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 1.83.
    te_: Seconds  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
    # 2.6.
    efd1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd1
    # (Se[Eefd1]).  Typical Value = 0.1.
    seefd1_: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
    # 3.45.
    efd2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd2
    # (Se[Efd2]).  Typical Value = 0.35.
    seefd2_: Simple_Float  = None
 
    # (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
    # true = a lower limit of zero is applied to integrator output
    # false = a lower limit of zero not applied to integrator output.
    # Typical Value = true.
    exclim_: bool  = None
 
    # Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99.
    edfmax_: PU  = None
 
    # Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99.
    efdmin_: PU  = None
 
    # (Efdlim).
    # true = exciter output limiter is active
    # false = exciter output limiter not active.
    # Typical Value = true.
    efdlim_: bool  = None
     