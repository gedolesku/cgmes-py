from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    efdmax: PU  = None
 
    # Field voltage clipping limit (Efdmin). 
    efdmin: PU  = None
 
    # Maximum field voltage output (Emax).  Typical Value = 20.
    emax: PU  = None
 
    # Minimum field voltage output (Emin).  Typical Value = -20.
    emin: PU  = None
 
    # Gain (K).  Typical Value = 1.
    k: PU  = None
 
    # Parameter of underexcitation limit (K1).  Typical Value = 0.1364.
    k1: PU  = None
 
    # Parameter of underexcitation limit (K2).  Typical Value = -0.3861.
    k2: PU  = None
 
    # PI controller gain (Kc).  Typical Value = 70.
    kc: PU  = None
 
    # Rectifier regulation factor (Kce).  Typical Value = 0.
    kce: PU  = None
 
    # Exciter internal reactance (Kd).  Typical Value = 0.
    kd: PU  = None
 
    # P controller gain (Kgob).  Typical Value = 10.
    kgob: PU  = None
 
    # PI controller gain (Kp).  Typical Value = 1.
    kp: PU  = None
 
    # PI controller gain of integral component (Kqi).  Typical Value = 0.
    kqi: PU  = None
 
    # Rate of rise of the reactive power (Kqob). 
    kqob: PU  = None
 
    # PI controller gain (Kqp).  Typical Value = 0.
    kqp: PU  = None
 
    # Dead band of reactive power (nq).  Determines the range of sensitivity.
    # Typical Value = 0.001.
    nq: PU  = None
 
    # Secondary voltage control state (Qc_on_off).
    # true = secondary voltage control is ON
    # false = secondary voltage control is OFF.
    # Typical Value = false.
    qconoff: bool  = None
 
    # Desired value (setpoint) of reactive power, manual setting (Qz). 
    qz: PU  = None
 
    # Selector to apply automatic calculation in secondary controller model.
    # true = automatic calculation is activated
    # false = manual set is active; the use of desired value of reactive power (Qz)
    # is required.
    # Typical Value = true.
    remote: bool  = None
 
    # Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259.
    sbase: ApparentPower  = None
 
    # PI controller phase lead time constant (Tc).  Typical Value = 8.
    tc: Seconds  = None
 
    # Time constant of gain block (Te).  Typical Value = 0.1.
    te: Seconds  = None
 
    # PI controller phase lead time constant (Ti).  Typical Value = 2.
    ti: Seconds  = None
 
    # Time constant (Tp).  Typical Value = 0.1.
    tp: Seconds  = None
 
    # Voltage transducer time constant (Tr).  Typical Value = 0.01.
    tr: Seconds  = None
 
    # Maximum error (Uimax).  Typical Value = 10.
    uimax: PU  = None
 
    # Minimum error (UImin).  Typical Value = -10.
    uimin: PU  = None
 
    # Maximum controller output (URmax).  Typical Value = 10.
    urmax: PU  = None
 
    # Minimum controller output (URmin).  Typical Value = -10.
    urmin: PU  = None
 
    # Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead
    # band.  Typical Value = 1.05.
    vtmax: PU  = None
 
    # Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead
    # band.  Typical Value = 0.95.
    vtmin: PU  = None
 
    # Maximum output (Yp).  Minimum output = 0.  Typical Value = 1.
    yp: PU  = None
     