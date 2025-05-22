from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcDC2A(ExcitationSystemDynamics):
    """Modified IEEE DC2A direct current commutator exciters with speed input, one
    more leg block in feedback loop and without underexcitation limiters (UEL)
    inputs.  DC type 2 excitation system model with added speed multiplier, added
    lead-lag, and voltage-dependent limits.
    """
    # Voltage regulator gain (Ka).  Typical Value = 300.
    ka_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.01.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 4.95.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -4.9.
    vrmin_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  If Ke is entered as zero,
    # the model calculates an effective value of Ke such that the initial condition
    # value of Vr is zero. The zero value of Ke is not changed.  If Ke is entered as
    # non-zero, its value is used directly, without change.  Typical Value = 1.
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 1.33.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675.
    tf_: Seconds  = None
 
    # Excitation control system stabilizer time constant (Tf1).  Typical Value = 0.
    tf1_: Seconds  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
    # 3.05.
    efd1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd1
    # (Se[Eefd1]).  Typical Value = 0.279.
    seefd1_: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
    # 2.29.
    efd2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd2
    # (Se[Efd2]).  Typical Value = 0.117.
    seefd2_: Simple_Float  = None
 
    # (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
    # true = a lower limit of zero is applied to integrator output
    # false = a lower limit of zero is not applied to integrator output.
    # Typical Value = true.
    exclim_: bool  = None
 
    # (Vtlim).
    # true = limiter at the block [Ka/(1+sTa)] is dependent on Vt
    # false = limiter at the block is not dependent on Vt.
    # Typical Value = true.
    vtlim_: bool  = None
     