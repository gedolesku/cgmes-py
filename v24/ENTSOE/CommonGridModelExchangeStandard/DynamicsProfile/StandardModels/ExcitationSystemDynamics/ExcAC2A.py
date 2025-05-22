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
class ExcAC2A(ExcitationSystemDynamics):
    """Modified IEEE AC2A alternator-supplied rectifier excitation system with
    different field current limit.
    """
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>c</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Voltage regulator gain (Ka).  Typical Value = 400.
    ka_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.02.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>amax</sub>).  Typical Value = 8.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>amin</sub>).  Typical Value = -8.
    vamin_: PU  = None
 
    # Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.
    # Typical Value = 25.
    kb_: PU  = None
 
    # Second stage regulator gain (Kb1). It is exciter field current controller gain
    # used as alternative to Kb to represent a variant of the ExcAC2A model.  Typical
    # Value = 25.
    kb1_: PU  = None
 
    # Maximum voltage regulator outputs (Vrmax).  Typical Value = 105.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (Vrmin).  Typical Value = -95.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 0.6.
    te_: Seconds  = None
 
    # Exciter field current limit reference (Vfemax).  Typical Value = 4.4.
    vfemax_: PU  = None
 
    # Exciter field current feedback gain (Kh).  Typical Value = 1.
    kh_: PU  = None
 
    # Excitation control system stabilizer gains (Kf).  Typical Value = 0.03.
    kf_: PU  = None
 
    # Exciter field current limiter gain (Kl).  Typical Value = 10.
    kl_: PU  = None
 
    # Maximum exciter field current (Vlr).  Typical Value = 4.4.
    vlr_: PU  = None
 
    # Coefficient to allow different usage of the model (Kl1).  Typical Value = 1.
    kl1_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc).  Typical
    # Value = 0.28.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances (Kd).
    # Typical Value = 0.35.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve<sub>1</sub>).  Typical Value = 4.4.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]).  Typical
    # Value = 0.037.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve<sub>2</sub>).  Typical Value = 3.3.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]).  Typical
    # Value = 0.012.
    seve2_: Simple_Float  = None
 
    # Indicates if HV gate is active (HVgate).
    # true = gate is used
    # false = gate is not used.
    # Typical Value = true.
    hvgate_: bool  = None
 
    # Indicates if LV gate is active (LVgate).
    # true = gate is used
    # false = gate is not used.
    # Typical Value = true.
    lvgate_: bool  = None
     