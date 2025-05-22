from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcST3A(ExcitationSystemDynamics):
    """Modified IEEE ST3A static excitation system with added speed multiplier.
    """
    # Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2.
    vimax_: PU  = None
 
    # Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2.
    vimin_: PU  = None
 
    # AVR gain (Kj).  Typical Value = 200.
    kj_: PU  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 6.67.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 1.
    tc_: Seconds  = None
 
    # Maximum AVR output (Efdmax).  Typical Value = 6.9.
    efdmax_: PU  = None
 
    # Forward gain constant of the inner loop field regulator (Km).  Typical Value =
    # 7.04.
    km_: PU  = None
 
    # Forward time constant of inner loop field regulator (Tm).  Typical Value = 1.
    tm_: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Feedback gain constant of the inner loop field regulator (Kg).  Typical Value =
    # 1.
    kg_: PU  = None
 
    # Potential source gain (Kp) (>0).  Typical Value = 4.37.
    kp_: PU  = None
 
    # Potential circuit phase angle (thetap).  Typical Value = 20.
    thetap_: AngleDegrees  = None
 
    # Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
    ki_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc). Typical
    # Value = 1.1.
    kc_: PU  = None
 
    # Reactance associated with potential source (Xl).  Typical Value = 0.09.
    xl_: PU  = None
 
    # Maximum excitation voltage (Vbmax).  Typical Value = 8.63.
    vbmax_: PU  = None
 
    # Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53.
    vgmax_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks1).
    # Typical Value = 0.
    ks1_: PU  = None
     