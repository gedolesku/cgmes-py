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
class GovSteamFV3(TurbineGovernorDynamics):
    """Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast
    valving.
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Governor gain, (reciprocal of droop) (K).  Typical Value = 20.
    k_: PU  = None
 
    # Governor lead time constant (T1).  Typical Value = 0.
    t1_: Seconds  = None
 
    # Governor lag time constant (T2).  Typical Value = 0.
    t2_: Seconds  = None
 
    # Valve positioner time constant (T3).  Typical Value = 0.
    t3_: Seconds  = None
 
    # Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1.
    uo_: Simple_Float  = None
 
    # Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1.
    uc_: Simple_Float  = None
 
    # Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1.
    pmax_: PU  = None
 
    # Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0.
    pmin_: PU  = None
 
    # Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2.
    t4_: Seconds  = None
 
    # Fraction of turbine power developed after first boiler pass (K1).  Typical
    # Value = 0.2.
    k1_: PU  = None
 
    # Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5.
    t5_: Seconds  = None
 
    # Fraction of turbine power developed after second boiler pass (K2).  Typical
    # Value = 0.2.
    k2_: PU  = None
 
    # Time constant of crossover or third boiler pass (T6).  Typical Value = 10.
    t6_: Seconds  = None
 
    # Fraction of hp turbine power developed after crossover or third boiler pass
    # (K3). Typical Value = 0.6.
    k3_: PU  = None
 
    # Time to close intercept valve (IV) (Ta).  Typical Value = 0.97.
    ta_: Seconds  = None
 
    # Time until IV starts to reopen (Tb).  Typical Value = 0.98.
    tb_: Seconds  = None
 
    # Time until IV is fully open (Tc).  Typical Value = 0.99.
    tc_: Seconds  = None
 
    # Max. pressure in reheater (Prmax).  Typical Value = 1.
    prmax_: PU  = None
     