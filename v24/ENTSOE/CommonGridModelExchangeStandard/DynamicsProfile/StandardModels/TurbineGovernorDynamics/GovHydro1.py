from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydro1(TurbineGovernorDynamics):
    """Basic Hydro turbine governor model.
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase: ActivePower  = None
 
    # Permanent droop (R) (>0).  Typical Value = 0.04.
    rperm: PU  = None
 
    # Temporary droop (r) (>R).  Typical Value = 0.3.
    rtemp: PU  = None
 
    # Washout time constant (Tr) (>0).  Typical Value = 5.
    tr: Seconds  = None
 
    # Filter time constant (<i>Tf</i>) (>0).  Typical Value = 0.05.
    tf: Seconds  = None
 
    # Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
    tg: Seconds  = None
 
    # Maximum gate velocity (Vlem) (>0).  Typical Value = 0.2.
    velm: Simple_Float  = None
 
    # Maximum gate opening (Gmax) (>0).  Typical Value = 1.
    gmax: PU  = None
 
    # Minimum gate opening (Gmin) (>=0).  Typical Value = 0.
    gmin: PU  = None
 
    # Water inertia time constant (Tw) (>0).  Typical Value = 1.
    tw: Seconds  = None
 
    # Turbine gain (At) (>0).  Typical Value = 1.2.
    at: PU  = None
 
    # Turbine damping factor (Dturb) (>=0).  Typical Value = 0.5.
    dturb: PU  = None
 
    # No-load flow at nominal head (qnl) (>=0).  Typical Value = 0.08.
    qnl: PU  = None
 
    # Turbine nominal head (hdam).  Typical Value = 1.
    hdam: PU  = None
     