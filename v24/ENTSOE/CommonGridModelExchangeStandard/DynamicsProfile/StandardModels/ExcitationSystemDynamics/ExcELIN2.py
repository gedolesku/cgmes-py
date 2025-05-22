from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcELIN2(ExcitationSystemDynamics):
    """Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-
    static excitation system. A PI voltage controller establishes a desired field
    current set point for a proportional current controller. The integrator of the
    PI controller has a follow-up input to match its signal to the present field
    current.  Power system stabilizer models used in conjunction with this
    excitation system model: PssELIN2, PssIEEE2B, Pss2B.
    """
    # Voltage regulator input gain (K1).  Typical Value = 0.
    k1_: PU  = None
 
    # Voltage regulator input limit (K1ec).  Typical Value = 2.
    k1ec_: PU  = None
 
    # Voltage controller derivative gain (Kd1).  Typical Value = 34.5.
    kd1_: PU  = None
 
    # Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.
    # 45.
    tb1_: Seconds  = None
 
    # Controller follow up gain (PID1max).  Typical Value = 2.
    pid1max_: PU  = None
 
    # Controller follow up dead band (Ti1).  Typical Value = 0.
    ti1_: PU  = None
 
    # Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5.
    iefmax2_: PU  = None
 
    # Gain (K2).  Typical Value = 5.
    k2_: PU  = None
 
    # Gain (Ketb).  Typical Value = 0.06.
    ketb_: PU  = None
 
    # Limiter (Upmax).  Typical Value = 3.
    upmax_: PU  = None
 
    # Limiter (Upmin).  Typical Value = 0.
    upmin_: PU  = None
 
    # Time constant (Te).  Typical Value = 0.
    te_: Seconds  = None
 
    # Excitation transformer effective reactance (Xp).  Typical Value = 1.
    xp_: PU  = None
 
    # Time Constant (Te2).  Typical Value = 1.
    te2_: Seconds  = None
 
    # Gain (Ke2).  Typical Value = 0.1.
    ke2_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve1).  Typical Value = 3.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Ve1,
    # back of commutating reactance (Se[Ve1]).  Typical Value = 0.
    seve1_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (Ve2).  Typical Value = 0.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Ve2,
    # back of commutating reactance (Se[Ve2]).  Typical Value = 1.
    seve2_: PU  = None
 
    # Time constant (Tr4).  Typical Value = 1.
    tr4_: Seconds  = None
 
    # Gain (K3).  Typical Value = 0.1.
    k3_: PU  = None
 
    # Time constant (Ti3).  Typical Value = 3.
    ti3_: Seconds  = None
 
    # Gain (K4).  Typical Value = 0.
    k4_: PU  = None
 
    # Time constant (Ti4).  Typical Value = 0.
    ti4_: Seconds  = None
 
    # Limiter (Iefmax).  Typical Value = 1.
    iefmax_: PU  = None
 
    # Limiter (Iefmin).  Typical Value = 1.
    iefmin_: PU  = None
 
    # Gain (Efdbas).  Typical Value = 0.1.
    efdbas_: PU  = None
     