from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcST2A(ExcitationSystemDynamics):
    """Modified IEEE ST2A static excitation system - another lead-lag block added to
    match  the model defined by WECC.
    """
    # Voltage regulator gain (Ka).  Typical Value = 120.
    ka_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.15.
    ta_: Seconds  = None
 
    # Maximum voltage regulator outputs (Vrmax).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (Vrmin).  Typical Value = -1.
    vrmin_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 0.5.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gains (Kf).  Typical Value = 0.05.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7.
    tf_: Seconds  = None
 
    # Potential circuit gain coefficient (Kp).  Typical Value = 4.88.
    kp_: PU  = None
 
    # Potential circuit gain coefficient (Ki).  Typical Value = 8.
    ki_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc).  Typical
    # Value = 1.82.
    kc_: PU  = None
 
    # Maximum field voltage (Efdmax).  Typical Value = 99.
    efdmax_: PU  = None
 
    # UEL input (UELin).
    # true = HV gate
    # false = add to error signal.
    # Typical Value = false.
    uelin_: bool  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
     