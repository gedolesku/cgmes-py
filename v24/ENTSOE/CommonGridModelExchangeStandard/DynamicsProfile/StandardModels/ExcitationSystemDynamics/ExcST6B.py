from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcST6BOELselectorKind import ExcST6BOELselectorKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcST6B(ExcitationSystemDynamics):
    """Modified IEEE ST6B static excitation system with PID controller and optional
    inner feedbacks loop.
    """
    # Exciter output current limit reference (Ilr).  Typical Value = 4.164.
    ilr_: PU  = None
 
    # Selector (K1).
    # true = feedback is from Ifd
    # false = feedback is not from Ifd.
    # Typical Value = true.
    k1_: bool  = None
 
    # Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577.
    kcl_: PU  = None
 
    # Pre-control gain constant of the inner loop field regulator (Kff).  Typical
    # Value = 1.
    kff_: PU  = None
 
    # Feedback gain constant of the inner loop field regulator (Kg).  Typical Value =
    # 1.
    kg_: PU  = None
 
    # Voltage regulator integral gain (Kia).  Typical Value = 45.094.
    kia_: PU  = None
 
    # Exciter output current limit adjustment (Kcl).  Typical Value = 17.33.
    klr_: PU  = None
 
    # Forward gain constant of the inner loop field regulator (Km).  Typical Value =
    # 1.
    km_: PU  = None
 
    # Voltage regulator proportional gain (Kpa).  Typical Value = 18.038.
    kpa_: PU  = None
 
    # Voltage regulator derivative gain (Kvd).  Typical Value = 0.
    kvd_: PU  = None
 
    # OEL input selector (OELin). Typical Value = noOELinput.
    oelin_: ExcST6BOELselectorKind  = None
 
    # Feedback time constant of inner loop field voltage regulator (Tg).  Typical
    # Value = 0.02.
    tg_: Seconds  = None
 
    # Rectifier firing time constant (Ts).  Typical Value = 0.
    ts_: Seconds  = None
 
    # Voltage regulator derivative gain (Tvd).  Typical Value = 0.
    tvd_: Seconds  = None
 
    # Maximum voltage regulator output (Vamax).  Typical Value = 4.81.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (Vamin).  Typical Value = -3.85.
    vamin_: PU  = None
 
    # Selector (Vilim).
    # true = Vimin-Vimax limiter is active
    # false = Vimin-Vimax limiter is not active.
    # Typical Value = true.
    vilim_: bool  = None
 
    # Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
    vimax_: PU  = None
 
    # Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
    vimin_: PU  = None
 
    # Selector (Vmult).
    # true = multiply regulator output by terminal voltage
    # false = do not multiply regulator output by terminal voltage.
    # Typical Value = true.
    vmult_: bool  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 4.81.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -3.85.
    vrmin_: PU  = None
 
    # Excitation source reactance (Xc).  Typical Value = 0.05.
    xc_: PU  = None
     