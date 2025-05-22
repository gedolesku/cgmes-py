from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcDC3A1(ExcitationSystemDynamics):
    """This is modified old IEEE type 3 excitation system.
    """
    # Voltage regulator gain (Ka).  Typical Value = 300.
    ka_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.01.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 5.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 1.83.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675.
    tf_: Seconds  = None
 
    # Potential circuit gain coefficient (Kp).  Typical Value = 4.37.
    kp_: PU  = None
 
    # Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
    ki_: PU  = None
 
    # Available exciter voltage limiter (Vbmax).  Typical Value = 11.63.
    vbmax_: PU  = None
 
    # (exclim).
    # true = lower limit of zero is applied to integrator output
    # false = lower limit of zero not applied to integrator output.
    # Typical Value = true.
    exclim_: bool  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Available exciter voltage limiter (Vb1max).  Typical Value = 11.63.
    vb1max_: PU  = None
 
    # Vb limiter indicator.
    # true = exciter Vbmax limiter is active
    # false = Vb1max is active.
    # Typical Value = true.
    vblim_: bool  = None
     