from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcST7BOELselectorKind import ExcST7BOELselectorKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcST7BUELselectorKind import ExcST7BUELselectorKind     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcST7B(ExcitationSystemDynamics):
    """Modified IEEE ST7B static excitation system without stator current limiter
    (SCL) and current compensator (DROOP) inputs.
    """
    # High-value gate feedback gain (Kh).  Typical Value = 1.
    kh_: PU  = None
 
    # Voltage regulator integral gain (Kia).  Typical Value = 1.
    kia_: PU  = None
 
    # Low-value gate feedback gain (Kl).  Typical Value = 1.
    kl_: PU  = None
 
    # Voltage regulator proportional gain (Kpa).  Typical Value = 40.
    kpa_: PU  = None
 
    # OEL input selector (OELin). Typical Value = noOELinput.
    oelin_: ExcST7BOELselectorKind  = None
 
    # Regulator lag time constant (Tb).  Typical Value = 1.
    tb_: Seconds  = None
 
    # Regulator lead time constant (Tc).  Typical Value = 1.
    tc_: Seconds  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Feedback time constant of inner loop field voltage regulator (Tg).  Typical
    # Value = 1.
    tg_: Seconds  = None
 
    # Feedback time constant (Tia).  Typical Value = 3.
    tia_: Seconds  = None
 
    # Rectifier firing time constant (Ts).  Typical Value = 0.
    ts_: Seconds  = None
 
    # UEL input selector (UELin). Typical Value = noUELinput.
    uelin_: ExcST7BUELselectorKind  = None
 
    # Maximum voltage reference signal (Vmax).  Typical Value = 1.1.
    vmax_: PU  = None
 
    # Minimum voltage reference signal (Vmin).  Typical Value = 0.9.
    vmin_: PU  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 5.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -4.5.
    vrmin_: PU  = None
     