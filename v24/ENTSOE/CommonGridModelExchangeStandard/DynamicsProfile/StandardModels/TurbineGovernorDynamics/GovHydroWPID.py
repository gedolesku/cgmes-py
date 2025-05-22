from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    mwbase: ActivePower  = None
 
    # Speed detector time constant (Treg).
    treg: Seconds  = None
 
    # Permanent drop (Reg).
    reg: PU  = None
 
    # Proportional gain (Kp).  Typical Value = 0.1.
    kp: PU  = None
 
    # Reset gain (Ki).  Typical Value = 0.36.
    ki: PU  = None
 
    # Derivative gain (Kd).  Typical Value = 1.11.
    kd: PU  = None
 
    # Controller time constant (Ta) (>0).  Typical Value = 0.
    ta: Seconds  = None
 
    # Gate servo time constant (Tb) (>0).  Typical Value = 0.
    tb: Seconds  = None
 
    # Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
    velmax: PU  = None
 
    # Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
    velmin: PU  = None
 
    # Gate opening Limit Maximum (Gatmax).
    gatmax: PU  = None
 
    # Gate opening Limit Minimum (Gatmin).
    gatmin: PU  = None
 
    # Water inertia time constant (Tw) (>0).  Typical Value = 0.
    tw: Seconds  = None
 
    # Maximum Power Output (Pmax).
    pmax: PU  = None
 
    # Minimum Power Output (Pmin).
    pmin: PU  = None
 
    # Turbine damping factor (D).  Unit = delta P / delta speed.
    d: PU  = None
 
    # Gate position 3 (Gv3).
    gv3: PU  = None
 
    # Gate position 1 (Gv1).
    gv1: PU  = None
 
    # Output at Gv1 PU of MWbase (Pgv1).
    pgv1: PU  = None
 
    # Gate position 2 (Gv2). 
    gv2: PU  = None
 
    # Output at Gv2 PU of MWbase (Pgv2).
    pgv2: PU  = None
 
    # Output at Gv3 PU of MWbase (Pgv3). 
    pgv3: PU  = None
     