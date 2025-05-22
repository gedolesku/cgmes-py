from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAC6A(ExcitationSystemDynamics):
    """Modified IEEE AC6A alternator-supplied rectifier excitation system with speed
    input.
    """
    # Voltage regulator gain (Ka).  Typical Value = 536.
    ka_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.086.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (Tk).  Typical Value = 0.18.
    tk_: Seconds  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 9.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 3.
    tc_: Seconds  = None
 
    # Maximum voltage regulator output (Vamax).  Typical Value = 75.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (Vamin).  Typical Value = -75.
    vamin_: PU  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 44.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -36.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 1.
    te_: Seconds  = None
 
    # Exciter field current limiter gain (Kh).  Typical Value = 92.
    kh_: PU  = None
 
    # Exciter field current limiter time constant (Tj).  Typical Value = 0.02.
    tj_: Seconds  = None
 
    # Exciter field current limiter time constant (Th).  Typical Value = 0.08.
    th_: Seconds  = None
 
    # Exciter field current limit reference (Vfelim).  Typical Value = 19.
    vfelim_: PU  = None
 
    # Maximum field current limiter signal reference (Vhmax).  Typical Value = 75.
    vhmax_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc).  Typical
    # Value = 0.173.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances (Kd).
    # Typical Value = 1.91.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.6.
    ke_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve<sub>1</sub>).  Typical Value = 7.4.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Ve1,
    # back of commutating reactance (Se[Ve1]).  Typical Value = 0.214.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve2).  Typical Value = 5.55.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Ve2,
    # back of commutating reactance (Se[Ve2]).  Typical Value = 0.044.
    seve2_: Simple_Float  = None
     