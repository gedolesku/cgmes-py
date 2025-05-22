from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydro2(TurbineGovernorDynamics):
    """IEEE hydro turbine governor model represents plants with straightforward
    penstock configurations and hydraulic-dashpot governors.
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase: ActivePower  = None
 
    # Gate servo time constant (Tg).  Typical Value = 0.5.
    tg: Seconds  = None
 
    # Pilot servo valve time constant (Tp).  Typical Value = 0.03.
    tp: Seconds  = None
 
    # Maximum gate opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1.
    uo: Simple_Float  = None
 
    # Maximum gate closing velocity (Uc) (<0).  Unit = PU/sec.   Typical Value = -0.1.
    uc: Simple_Float  = None
 
    # Maximum gate opening (Pmax).  Typical Value = 1.
    pmax: PU  = None
 
    # Minimum gate opening; (<i>Pmin</i>).  Typical Value = 0.
    pmin: PU  = None
 
    # Permanent droop (Rperm).  Typical Value = 0.05.
    rperm: PU  = None
 
    # Temporary droop (Rtemp).  Typical Value = 0.5.
    rtemp: PU  = None
 
    # Dashpot time constant (Tr).  Typical Value = 12.
    tr: Seconds  = None
 
    # Water inertia time constant (Tw).  Typical Value = 2.
    tw: Seconds  = None
 
    # Turbine gain (Kturb).  Typical Value = 1.
    kturb: PU  = None
 
    # Turbine numerator multiplier (Aturb).  Typical Value = -1.
    aturb: PU  = None
 
    # Turbine denominator multiplier (Bturb).  Typical Value = 0.5.
    bturb: PU  = None
 
    # Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
    db1: Frequency  = None
 
    # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    eps: Frequency  = None
 
    # Unintentional deadband (db2).  Unit = MW.  Typical Value = 0.
    db2: ActivePower  = None
 
    # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
    gv1: PU  = None
 
    # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
    pgv1: PU  = None
 
    # Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
    gv2: PU  = None
 
    # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
    pgv2: PU  = None
 
    # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
    gv3: PU  = None
 
    # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
    pgv3: PU  = None
 
    # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
    gv4: PU  = None
 
    # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
    pgv4: PU  = None
 
    # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
    gv5: PU  = None
 
    # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
    pgv5: PU  = None
 
    # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
    gv6: PU  = None
 
    # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
    pgv6: PU  = None
     