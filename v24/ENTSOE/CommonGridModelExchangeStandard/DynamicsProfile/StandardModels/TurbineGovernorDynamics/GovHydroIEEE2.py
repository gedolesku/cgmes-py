from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroIEEE2(TurbineGovernorDynamics):
    """IEEE hydro turbine governor model represents plants with straightforward
    penstock configurations and hydraulic-dashpot governors.
    
      Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and
    Systems</font>
      <font color="#0f0f0f">November/December 1973, Volume PAS-92, Number 6</font>
      <font color="#0f0f0f"><i><u>Dynamic Models for Steam and Hydro Turbines in
    Power System Studies</u></i>, Page 1904.</font>
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Gate servo time constant (Tg).  Typical Value = 0.5.
    tg_: Seconds  = None
 
    # Pilot servo valve time constant (Tp).  Typical Value = 0.03.
    tp_: Seconds  = None
 
    # Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1.
    uo_: Simple_Float  = None
 
    # Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1.
    uc_: Simple_Float  = None
 
    # Maximum gate opening (Pmax).  Typical Value = 1.
    pmax_: PU  = None
 
    # Minimum gate opening (Pmin).  Typical Value = 0.
    pmin_: PU  = None
 
    # Permanent droop (Rperm).  Typical Value = 0.05.
    rperm_: PU  = None
 
    # Temporary droop (Rtemp).  Typical Value = 0.5.
    rtemp_: PU  = None
 
    # Dashpot time constant (Tr).  Typical Value = 12.
    tr_: Seconds  = None
 
    # Water inertia time constant (Tw).  Typical Value = 2.
    tw_: Seconds  = None
 
    # Turbine gain (Kturb).  Typical Value = 1.
    kturb_: PU  = None
 
    # Turbine numerator multiplier (Aturb).  Typical Value = -1.
    aturb_: PU  = None
 
    # Turbine denominator multiplier (Bturb).  Typical Value = 0.5.
    bturb_: PU  = None
 
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
     