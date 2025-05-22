from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcDC1A(ExcitationSystemDynamics):
    """Modified IEEE DC1A direct current commutator exciter with speed input and
    without underexcitation limiters (UEL) inputs.
    """
    # Voltage regulator gain (Ka).  Typical Value = 46.
    ka_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.06.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -0.9.
    vrmin_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 0.
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 0.46.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
    # 3.1.
    efd1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd1
    # (Se[Eefd1]).  Typical Value = 0.33.
    seefd1_: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
    # 2.3.
    efd2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd1
    # (Se[Eefd1]).  Typical Value = 0.33.
    seefd2_: Simple_Float  = None
 
    # (exclim).
    # IEEE standard is ambiguous about lower limit on exciter output.
    # true = a lower limit of zero is applied to integrator output
    # false = a lower limit of zero is not applied to integrator output.
    # Typical Value = true.
    exclim_: bool  = None
 
    # Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99.
    efdmin_: PU  = None
 
    # Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99.
    edfmax_: PU  = None
     