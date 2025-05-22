from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcST4B(ExcitationSystemDynamics):
    """Modified IEEE ST4B static excitation system with maximum inner loop feedback
    gain <b>Vgmax</b>.
    """
    # Voltage regulator proportional gain (Kpr).  Typical Value = 10.75.
    kpr_: PU  = None
 
    # Voltage regulator integral gain (Kir).  Typical Value = 10.75.
    kir_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.02.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -0.87.
    vrmin_: PU  = None
 
    # Voltage regulator proportional gain output (Kpm).  Typical Value = 1.
    kpm_: PU  = None
 
    # Voltage regulator integral gain output (Kim).  Typical Value = 0.
    kim_: PU  = None
 
    # Maximum inner loop output (Vmmax).  Typical Value = 99.
    vmmax_: PU  = None
 
    # Minimum inner loop output (Vmmin).  Typical Value = -99.
    vmmin_: PU  = None
 
    # Feedback gain constant of the inner loop field regulator (Kg). Typical Value =
    # 0.
    kg_: PU  = None
 
    # Potential circuit gain coefficient (Kp).  Typical Value = 9.3.
    kp_: PU  = None
 
    # Potential circuit phase angle (thetap).  Typical Value = 0.
    thetap_: AngleDegrees  = None
 
    # Potential circuit gain coefficient (Ki).  Typical Value = 0.
    ki_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc). Typical
    # Value = 0.113.
    kc_: PU  = None
 
    # Reactance associated with potential source (Xl).  Typical Value = 0.124.
    xl_: PU  = None
 
    # Maximum excitation voltage (Vbmax).  Typical Value = 11.63.
    vbmax_: PU  = None
 
    # Maximum inner loop feedback voltage (Vgmax).  Typical Value = 5.8.
    vgmax_: PU  = None
 
    # Selector (Uel).
    # true = UEL is part of block diagram
    # false = UEL is not part of block diagram.
    # Typical Value = false.
    uel_: bool  = None
 
    # Selector (LVgate).
    # true = LVgate is part of the block diagram
    # false = LVgate is not part of the block diagram.
    # Typical Value = false.
    lvgate_: bool  = None
     