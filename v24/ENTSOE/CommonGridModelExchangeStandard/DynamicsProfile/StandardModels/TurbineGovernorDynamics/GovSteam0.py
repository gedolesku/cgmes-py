from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteam0(TurbineGovernorDynamics):
    """A simplified steam turbine governor model.
    """
    # Base for power values (MWbase)  (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Permanent droop (R).  Typical Value = 0.05.
    r_: PU  = None
 
    # Steam bowl time constant (T1).  Typical Value = 0.5.
    t1_: Seconds  = None
 
    # Maximum valve position, PU of mwcap (Vmax).  Typical Value = 1.
    vmax_: PU  = None
 
    # Minimum valve position, PU of mwcap (Vmin).  Typical Value = 0.
    vmin_: PU  = None
 
    # Numerator time constant of T2/T3 block (T2).  Typical Value = 3.
    t2_: Seconds  = None
 
    # Reheater time constant (T3).  Typical Value = 10.
    t3_: Seconds  = None
 
    # Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical Value
    # = 0.
    dt_: PU  = None
     