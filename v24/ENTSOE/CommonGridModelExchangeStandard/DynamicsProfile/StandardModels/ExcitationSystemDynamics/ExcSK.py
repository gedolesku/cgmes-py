from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ApparentPower import ApparentPower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcSK(ExcitationSystemDynamics):
    """Slovakian Excitation System Model.  UEL and secondary voltage control are
    included in this model. When this model is used, there cannot be a separate
    underexcitation limiter or VAr controller model.
    """
    # Field voltage clipping limit (Efdmax). 
    efdmax_: PU  = None
 
    # Field voltage clipping limit (Efdmin). 
    efdmin_: PU  = None
 
    # Maximum field voltage output (Emax).  Typical Value = 20.
    emax_: PU  = None
 
    # Minimum field voltage output (Emin).  Typical Value = -20.
    emin_: PU  = None
 
    # Gain (K).  Typical Value = 1.
    k_: PU  = None
 
    # Parameter of underexcitation limit (K1).  Typical Value = 0.1364.
    k1_: PU  = None
 
    # Parameter of underexcitation limit (K2).  Typical Value = -0.3861.
    k2_: PU  = None
 
    # PI controller gain (Kc).  Typical Value = 70.
    kc_: PU  = None
 
    # Rectifier regulation factor (Kce).  Typical Value = 0.
    kce_: PU  = None
 
    # Exciter internal reactance (Kd).  Typical Value = 0.
    kd_: PU  = None
 
    # P controller gain (Kgob).  Typical Value = 10.
    kgob_: PU  = None
 
    # PI controller gain (Kp).  Typical Value = 1.
    kp_: PU  = None
 
    # PI controller gain of integral component (Kqi).  Typical Value = 0.
    kqi_: PU  = None
 
    # Rate of rise of the reactive power (Kqob). 
    kqob_: PU  = None
 
    # PI controller gain (Kqp).  Typical Value = 0.
    kqp_: PU  = None
 
    # Dead band of reactive power (nq).  Determines the range of sensitivity.
    # Typical Value = 0.001.
    nq_: PU  = None
 
    # Secondary voltage control state (Qc_on_off).
    # true = secondary voltage control is ON
    # false = secondary voltage control is OFF.
    # Typical Value = false.
    qconoff_: bool  = None
 
    # Desired value (setpoint) of reactive power, manual setting (Qz). 
    qz_: PU  = None
 
    # Selector to apply automatic calculation in secondary controller model.
    # true = automatic calculation is activated
    # false = manual set is active; the use of desired value of reactive power (Qz)
    # is required.
    # Typical Value = true.
    remote_: bool  = None
 
    # Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259.
    sbase_: ApparentPower  = None
 
    # PI controller phase lead time constant (Tc).  Typical Value = 8.
    tc_: Seconds  = None
 
    # Time constant of gain block (Te).  Typical Value = 0.1.
    te_: Seconds  = None
 
    # PI controller phase lead time constant (Ti).  Typical Value = 2.
    ti_: Seconds  = None
 
    # Time constant (Tp).  Typical Value = 0.1.
    tp_: Seconds  = None
 
    # Voltage transducer time constant (Tr).  Typical Value = 0.01.
    tr_: Seconds  = None
 
    # Maximum error (Uimax).  Typical Value = 10.
    uimax_: PU  = None
 
    # Minimum error (UImin).  Typical Value = -10.
    uimin_: PU  = None
 
    # Maximum controller output (URmax).  Typical Value = 10.
    urmax_: PU  = None
 
    # Minimum controller output (URmin).  Typical Value = -10.
    urmin_: PU  = None
 
    # Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead
    # band.  Typical Value = 1.05.
    vtmax_: PU  = None
 
    # Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead
    # band.  Typical Value = 0.95.
    vtmin_: PU  = None
 
    # Maximum output (Yp).  Minimum output = 0.  Typical Value = 1.
    yp_: PU  = None
     