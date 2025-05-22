from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAC3A(ExcitationSystemDynamics):
    """Modified IEEE AC3A alternator-supplied rectifier excitation system with
    different field current limit.
    """
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>c</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Voltage regulator gain (Ka).  Typical Value = 45.62.
    ka_: Seconds  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.013.
    ta_: PU  = None
 
    # Maximum voltage regulator output (V<sub>amax</sub>).  Typical Value = 1.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>amin</sub>).  Typical Value = -0.95.
    vamin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 1.17.
    te_: Seconds  = None
 
    # Minimum exciter voltage output (Vemin).  Typical Value = 0.1.
    vemin_: PU  = None
 
    # Constant associated with regulator and alternator field power supply (Kr).
    # Typical Value =3.77.
    kr_: PU  = None
 
    # Excitation control system stabilizer gains (Kf).  Typical Value = 0.143.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Excitation control system stabilizer gain (Kn).  Typical Value =0.05.
    kn_: PU  = None
 
    # Value of <i>EFD </i>at which feedback gain changes (Efdn).  Typical Value = 2.
    # 36.
    efdn_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc).  Typical
    # Value = 0.104.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances (Kd).
    # Typical Value = 0.499.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Gain used in the minimum field voltage limiter loop (Klv).  Typical Value = 0.
    # 194.
    klv_: PU  = None
 
    # Coefficient to allow different usage of the model (Kf1).  Typical Value = 1.
    kf1_: PU  = None
 
    # Coefficient to allow different usage of the model (Kf2).  Typical Value = 0.
    kf2_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Exciter field current limit reference (Vfemax).  Typical Value = 16.
    vfemax_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve1) equals Vemax (Ve1).  Typical Value = 6.24.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]).  Typical
    # Value = 1.143.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve<sub>2</sub>).  Typical Value = 4.68.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]).  Typical
    # Value = 0.1.
    seve2_: Simple_Float  = None
 
    # Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical
    # Value = 0.79.
    vlv_: PU  = None
     