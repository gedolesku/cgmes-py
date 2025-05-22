from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteamSGO(TurbineGovernorDynamics):
    """Simplified Steam turbine governor model.
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase: ActivePower  = None
 
    # Controller lag (T1).
    t1: Seconds  = None
 
    # Controller lead compensation (T2).
    t2: Seconds  = None
 
    # Governor lag (T3) (>0). 
    t3: Seconds  = None
 
    # Delay due to steam inlet volumes associated with steam chest and inlet piping
    # (T4). 
    t4: Seconds  = None
 
    # Reheater delay including hot and cold leads (T5). 
    t5: Seconds  = None
 
    # Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6). 
    t6: Seconds  = None
 
    # One/per unit regulation (K1). 
    k1: PU  = None
 
    # Fraction (K2). 
    k2: PU  = None
 
    # Fraction (K3).
    k3: PU  = None
 
    # Upper power limit (Pmax). 
    pmax: PU  = None
 
    # Lower power limit (Pmin).
    pmin: Seconds  = None
     