from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroWPID(TurbineGovernorDynamics):
    """Woodward PID Hydro Governor.
    """
    # Base for power values  (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Speed detector time constant (Treg).
    treg_: Seconds  = None
 
    # Permanent drop (Reg).
    reg_: PU  = None
 
    # Proportional gain (Kp).  Typical Value = 0.1.
    kp_: PU  = None
 
    # Reset gain (Ki).  Typical Value = 0.36.
    ki_: PU  = None
 
    # Derivative gain (Kd).  Typical Value = 1.11.
    kd_: PU  = None
 
    # Controller time constant (Ta) (>0).  Typical Value = 0.
    ta_: Seconds  = None
 
    # Gate servo time constant (Tb) (>0).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
    velmax_: PU  = None
 
    # Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
    velmin_: PU  = None
 
    # Gate opening Limit Maximum (Gatmax).
    gatmax_: PU  = None
 
    # Gate opening Limit Minimum (Gatmin).
    gatmin_: PU  = None
 
    # Water inertia time constant (Tw) (>0).  Typical Value = 0.
    tw_: Seconds  = None
 
    # Maximum Power Output (Pmax).
    pmax_: PU  = None
 
    # Minimum Power Output (Pmin).
    pmin_: PU  = None
 
    # Turbine damping factor (D).  Unit = delta P / delta speed.
    d_: PU  = None
 
    # Gate position 3 (Gv3).
    gv3_: PU  = None
 
    # Gate position 1 (Gv1).
    gv1_: PU  = None
 
    # Output at Gv1 PU of MWbase (Pgv1).
    pgv1_: PU  = None
 
    # Gate position 2 (Gv2). 
    gv2_: PU  = None
 
    # Output at Gv2 PU of MWbase (Pgv2).
    pgv2_: PU  = None
 
    # Output at Gv3 PU of MWbase (Pgv3). 
    pgv3_: PU  = None
     