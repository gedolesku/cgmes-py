from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcREXSFeedbackSignalKind import ExcREXSFeedbackSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcREXS(ExcitationSystemDynamics):
    """General Purpose Rotating Excitation System Model.  This model can be used to
    represent a wide range of excitation systems whose DC power source is an AC or
    DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system
    models.
    """
    # Field voltage value 1 (E1).  Typical Value = 3.
    e1_: PU  = None
 
    # Field voltage value 2 (E2).  Typical Value = 4.
    e2_: PU  = None
 
    # Rate feedback signal flag (Fbf). Typical Value = fieldCurrent.
    fbf_: ExcREXSFeedbackSignalKind  = None
 
    # Limit type flag (Flimf).  Typical Value = 0.
    flimf_: PU  = None
 
    # Rectifier regulation factor (Kc).  Typical Value = 0.05.
    kc_: PU  = None
 
    # Exciter regulation factor (Kd).  Typical Value = 2.
    kd_: PU  = None
 
    # Exciter field proportional constant (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Field voltage feedback gain (Kefd).  Typical Value = 0.
    kefd_: PU  = None
 
    # Rate feedback gain (Kf).  Typical Value = 0.05.
    kf_: Seconds  = None
 
    # Field voltage controller feedback gain (Kh).  Typical Value = 0.
    kh_: PU  = None
 
    # Field Current Regulator Integral Gain (Kii).  Typical Value = 0.
    kii_: PU  = None
 
    # Field Current Regulator Proportional Gain (Kip).  Typical Value = 1.
    kip_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Voltage Regulator Integral Gain (Kvi).  Typical Value = 0.
    kvi_: PU  = None
 
    # Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800.
    kvp_: PU  = None
 
    # V/Hz limiter gain (Kvphz).  Typical Value = 0.
    kvphz_: PU  = None
 
    # Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0.
    nvphz_: PU  = None
 
    # Saturation factor at E1 (Se1).  Typical Value = 0.0001.
    se1_: PU  = None
 
    # Saturation factor at E2 (Se2).  Typical Value = 0.001.
    se2_: PU  = None
 
    # Voltage Regulator time constant (Ta).  Typical Value = 0.01.
    ta_: Seconds  = None
 
    # Lag time constant (Tb1).  Typical Value = 0.
    tb1_: Seconds  = None
 
    # Lag time constant (Tb2).  Typical Value = 0.
    tb2_: Seconds  = None
 
    # Lead time constant (Tc1).  Typical Value = 0.
    tc1_: Seconds  = None
 
    # Lead time constant (Tc2).  Typical Value = 0.
    tc2_: Seconds  = None
 
    # Exciter field time constant (Te).  Typical Value = 1.2.
    te_: Seconds  = None
 
    # Rate feedback time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Feedback lead time constant (Tf1).  Typical Value = 0.
    tf1_: Seconds  = None
 
    # Feedback lag time constant (Tf2).  Typical Value = 0.
    tf2_: Seconds  = None
 
    # Field current Bridge time constant (Tp).  Typical Value = 0.
    tp_: Seconds  = None
 
    # Maximum compounding voltage (Vcmax).  Typical Value = 0.
    vcmax_: PU  = None
 
    # Maximum Exciter Field Current (Vfmax).  Typical Value = 47.
    vfmax_: PU  = None
 
    # Minimum Exciter Field Current (Vfmin).  Typical Value = -20.
    vfmin_: PU  = None
 
    # Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1.
    vimax_: PU  = None
 
    # Maximum controller output (Vrmax).  Typical Value = 47.
    vrmax_: PU  = None
 
    # Minimum controller output (Vrmin).  Typical Value = -20.
    vrmin_: PU  = None
 
    # Exciter compounding reactance (Xc).  Typical Value = 0.
    xc_: PU  = None
     