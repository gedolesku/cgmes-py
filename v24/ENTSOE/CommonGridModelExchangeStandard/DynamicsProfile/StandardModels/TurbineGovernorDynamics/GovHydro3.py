from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydro3(TurbineGovernorDynamics):
    """Modified IEEE Hydro Governor-Turbine Model.
    
      This model differs from that defined in the IEEE modeling guideline paper in
    that the limits on gate position and velocity do not permit "wind up" of the
    upstream signals.
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
    pmax_: PU  = None
 
    # Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
    pmin_: PU  = None
 
    # Governor control flag (Cflag).
    # true = PID control is active
    # false = double derivative control is active.
    # Typical Value = true.
    governorControl_: bool  = None
 
    # Steady-state droop, PU, for governor output feedback (Rgate).  Typical Value =
    # 0.
    rgate_: PU  = None
 
    # Steady-state droop, PU, for electrical power feedback (Relec).  Typical Value =
    # 0.05.
    relec_: PU  = None
 
    # Input filter time constant (Td).  Typical Value = 0.05.
    td_: Seconds  = None
 
    # Washout time constant (Tf).  Typical Value = 0.1.
    tf_: Seconds  = None
 
    # Gate servo time constant (Tp).  Typical Value = 0.05.
    tp_: Seconds  = None
 
    # Maximum gate opening velocity (Velop).  Unit = PU/sec. Typical Value = 0.2.
    velop_: Simple_Float  = None
 
    # Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2.
    velcl_: Simple_Float  = None
 
    # Derivative gain (K1).  Typical Value = 0.01.
    k1_: PU  = None
 
    # Double derivative gain, if Cflag = -1 (K2).  Typical Value = 2.5.
    k2_: PU  = None
 
    # Integral gain (Ki).  Typical Value = 0.5.
    ki_: PU  = None
 
    # Gate servo gain (Kg).  Typical Value = 2.
    kg_: PU  = None
 
    # Power feedback time constant (Tt).  Typical Value = 0.2.
    tt_: Seconds  = None
 
    # Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
    db1_: Frequency  = None
 
    # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    eps_: Frequency  = None
 
    # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    db2_: ActivePower  = None
 
    # Water inertia time constant (Tw).  Typical Value = 1.
    tw_: Seconds  = None
 
    # Turbine gain (At).  Typical Value = 1.2.
    at_: PU  = None
 
    # Turbine damping factor (Dturb).  Typical Value = 0.2.
    dturb_: PU  = None
 
    # No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08.
    qnl_: PU  = None
 
    # Turbine nominal head (H0).  Typical Value = 1.
    h0_: PU  = None
 
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
     