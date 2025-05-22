from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroPID(TurbineGovernorDynamics):
    """PID governor and turbine.
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
    pmax_: PU  = None
 
    # Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
    pmin_: PU  = None
 
    # Steady state droop (R).  Typical Value = 0.05.
    r_: PU  = None
 
    # Input filter time constant (Td).  Typical Value = 0.
    td_: Seconds  = None
 
    # Washout time constant (Tf).  Typical Value = 0.1.
    tf_: Seconds  = None
 
    # Gate servo time constant (Tp).  Typical Value = 0.35.
    tp_: Seconds  = None
 
    # Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.09.
    velop_: Simple_Float  = None
 
    # Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.14.
    velcl_: Simple_Float  = None
 
    # Derivative gain (Kd).  Typical Value = 1.11.
    kd_: PU  = None
 
    # Proportional gain (Kp).  Typical Value = 0.1.
    kp_: PU  = None
 
    # Integral gain (Ki).  Typical Value = 0.36.
    ki_: PU  = None
 
    # Gate servo gain (Kg).  Typical Value = 2.5.
    kg_: PU  = None
 
    # Turbine time constant (Tturb) (note 3).  Typical Value = 0.8.
    tturb_: Seconds  = None
 
    # Turbine numerator multiplier (Aturb) (note 3).  Typical Value -1.
    aturb_: PU  = None
 
    # Turbine denominator multiplier (Bturb) (note 3).  Typical Value = 0.5.
    bturb_: PU  = None
 
    # Power feedback time constant (Tt).  Typical Value = 0.02.
    tt_: Seconds  = None
 
    # Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
    db1_: Frequency  = None
 
    # Input signal switch (Flag).
    # true = Pe input is used
    # false = feedback is received from CV.
    # Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf
    # is not zero, Flag is set to true.  Typical Value = true.
    inputSignal_: bool  = None
 
    # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    eps_: Frequency  = None
 
    # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    db2_: ActivePower  = None
 
    # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
    gv1_: PU  = None
 
    # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
    pgv1_: PU  = None
 
    # Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
    gv2_: PU  = None
 
    # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
    pgv2_: PU  = None
 
    # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
    gv3_: PU  = None
 
    # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
    pgv3_: PU  = None
 
    # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
    gv4_: PU  = None
 
    # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
    pgv4_: PU  = None
 
    # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
    gv5_: PU  = None
 
    # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
    pgv5_: PU  = None
 
    # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
    gv6_: PU  = None
 
    # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
    pgv6_: PU  = None
     