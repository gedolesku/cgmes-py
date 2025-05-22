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
class ExcAC1A(ExcitationSystemDynamics):
    """Modified IEEE AC1A alternator-supplied rectifier excitation system with
    different rate feedback source.
    """
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>c</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Voltage regulator gain (Ka).  Typical Value = 400.
    ka_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.02.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>amax</sub>).  Typical Value = 14.5.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>amin</sub>).  Typical Value = -14.5.
    vamin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 0.8.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gains (Kf).  Typical Value = 0.03.
    kf_: PU  = None
 
    # Coefficient to allow different usage of the model (Kf1).  Typical Value = 0.
    kf1_: PU  = None
 
    # Coefficient to allow different usage of the model (Kf2).  Typical Value = 1.
    kf2_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc). Typical
    # Value = 0.2.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances (Kd).
    # Typical Value = 0.38.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve1).  Typical Value = 4.18.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Ve1,
    # back of commutating reactance (Se[Ve1]).  Typical Value = 0.1.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve2).  Typical Value = 3.14.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Ve2,
    # back of commutating reactance (Se[Ve2]).  Typical Value = 0.03.
    seve2_: Simple_Float  = None
 
    # Maximum voltage regulator outputs (Vrmax).  Typical Value = 6.03.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (Rrmin).  Typical Value = -5.43.
    vrmin_: PU  = None
 
    # Indicates if both HV gate and LV gate are active (HVLVgates).
    # true = gates are used
    # false = gates are not used.
    # Typical Value = true.
    hvlvgates_: bool  = None
     