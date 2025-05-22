from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteamFV2(TurbineGovernorDynamics):
    """Steam turbine governor with reheat time constants and modeling of the effects
    of fast valve closing to reduce mechanical power.
    """
    # Alternate Base used instead of Machine base in equipment model if necessary
    # (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # (R).
    r_: PU  = None
 
    # Governor time constant (T1).
    t1_: Seconds  = None
 
    # (Vmax).
    vmax_: PU  = None
 
    # (Vmin).
    vmin_: PU  = None
 
    # Fraction of the turbine power developed by turbine sections not involved in
    # fast valving (K).
    k_: PU  = None
 
    # Reheater time constant (T3).
    t3_: Seconds  = None
 
    # (Dt).
    dt_: PU  = None
 
    # Time constant with which power falls off after intercept valve closure (Tt).
    tt_: Seconds  = None
 
    # Time after initial time for valve to close (Ta).
    ta_: Seconds  = None
 
    # Time after initial time for valve to begin opening (Tb).
    tb_: Seconds  = None
 
    # Time after initial time for valve to become fully open (Tc).
    tc_: Seconds  = None
 
    # Initial time to begin fast valving (Ti).
    ti_: Seconds  = None
     