from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAC8B(ExcitationSystemDynamics):
    """Modified IEEE AC8B alternator-supplied rectifier excitation system with speed
    input and input limiter.
    """
    # Input limiter indicator.
    # true = input limiter Vimax and Vimin is considered
    # false = input limiter Vimax and Vimin is not considered.
    # Typical Value = true.
    inlim_: bool  = None
 
    # Voltage regulator gain (Ka).  Typical Value = 1.
    ka_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc). Typical
    # Value = 0.55.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances (Kd).
    # Typical Value = 1.1.
    kd_: PU  = None
 
    # Voltage regulator derivative gain (Kdr).  Typical Value = 10.
    kdr_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Voltage regulator integral gain (Kir).  Typical Value = 5.
    kir_: PU  = None
 
    # Voltage regulator proportional gain (Kpr).  Typical Value = 80.
    kpr_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # PID limiter indicator.
    # true = input limiter Vpidmax and Vpidmin is considered
    # false = input limiter Vpidmax and Vpidmin is not considered.
    # Typical Value = true.
    pidlim_: bool  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # Ve<sub>1</sub>, back of commutating reactance (Se[Ve1]).  Typical Value = 0.3.
    seve1_: Simple_Float  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # Ve<sub>2</sub>, back of commutating reactance (Se[Ve2]).  Typical Value = 3.
    seve2_: Simple_Float  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.
    ta_: Seconds  = None
 
    # Lag time constant (Tdr).  Typical Value = 0.1.
    tdr_: Seconds  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 1.2.
    te_: Seconds  = None
 
    # Selector for the limiter on the block [1/sTe].
    # See diagram for meaning of true and false.
    # Typical Value = false.
    telim_: bool  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve<sub>1</sub>) equals V<sub>EMAX</sub> (Ve1).  Typical
    # Value = 6.5.
    ve1_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve<sub>2</sub>).  Typical Value = 9.
    ve2_: PU  = None
 
    # Minimum exciter voltage output (Vemin).  Typical Value = 0.
    vemin_: PU  = None
 
    # Exciter field current limit reference (Vfemax).  Typical Value = 6.
    vfemax_: PU  = None
 
    # Input signal maximum (Vimax).  Typical Value = 35.
    vimax_: PU  = None
 
    # Input signal minimum (Vimin).  Typical Value = -10.
    vimin_: PU  = None
 
    # PID maximum controller output (Vpidmax).  Typical Value = 35.
    vpidmax_: PU  = None
 
    # PID minimum controller output (Vpidmin).  Typical Value = -10.
    vpidmin_: PU  = None
 
    # Maximum voltage regulator output (Vrmax). Typical Value = 35.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Multiply by generator's terminal voltage indicator.
    # true =the limits Vrmax and Vrmin are multiplied by the generator�s terminal
    # voltage to represent a thyristor power stage fed from the generator terminals
    # false = limits are not multiplied by generator's terminal voltage.
    # Typical Value = false.
    vtmult_: bool  = None
     