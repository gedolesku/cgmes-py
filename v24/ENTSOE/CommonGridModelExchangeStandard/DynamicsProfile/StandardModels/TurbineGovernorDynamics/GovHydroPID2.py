from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroPID2(TurbineGovernorDynamics):
    """Hydro turbine and governor. Represents plants with straight forward penstock
    configurations and "three term" electro-hydraulic governors (i.e. Woodard
    electronic).
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Speed detector time constant (Treg).  Typical Value = 0.
    treg_: Seconds  = None
 
    # Permanent drop (Rperm).  Typical Value = 0.
    rperm_: PU  = None
 
    # Proportional gain (Kp).  Typical Value = 0.
    kp_: PU  = None
 
    # Reset gain (Ki).  Unit = PU/ sec.  Typical Value = 0.
    ki_: Simple_Float  = None
 
    # Derivative gain (Kd).  Typical Value = 0.
    kd_: PU  = None
 
    # Controller time constant (Ta) (>0).  Typical Value = 0.
    ta_: Seconds  = None
 
    # Gate servo time constant (Tb) (>0).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0.
    velmax_: Simple_Float  = None
 
    # Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0.
    velmin_: Simple_Float  = None
 
    # Maximum gate opening (Gmax).  Typical Value = 0.
    gmax_: PU  = None
 
    # Minimum gate opening (Gmin).  Typical Value = 0.
    gmin_: PU  = None
 
    # Water inertia time constant (Tw) (>0).  Typical Value = 0.
    tw_: Seconds  = None
 
    # Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0.
    d_: PU  = None
 
    # Gate opening at speed no load (G0).  Typical Value = 0.
    g0_: PU  = None
 
    # Intermediate gate opening (G1).  Typical Value = 0.
    g1_: PU  = None
 
    # Power at gate opening G1 (P1).  Typical Value = 0.
    p1_: PU  = None
 
    # Intermediate gate opening (G2).  Typical Value = 0.
    g2_: PU  = None
 
    # Power at gate opening G2 (P2).  Typical Value = 0.
    p2_: PU  = None
 
    # Power at full opened gate (P3).  Typical Value = 0.
    p3_: PU  = None
 
    # Factor multiplying Tw (Atw).  Typical Value = 0.
    atw_: PU  = None
 
    # Feedback signal type flag (Flag).
    # true = use gate position feedback signal
    # false = use Pe.
    feedbackSignal_: bool  = None
     