from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroIEEE0(TurbineGovernorDynamics):
    """IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic
    and Electro-Hydraulic turbine governors, with our without steam feedback.
    Typical values given are for Mechanical-Hydraulic.
    
      Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and
    Systems</font>
      <font color="#0f0f0f">November/December 1973, Volume PAS-92, Number 6</font>
      <font color="#0f0f0f"><i><u>Dynamic Models for Steam and Hydro Turbines in
    Power System Studies</u></i>, Page 1904.</font>
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase: ActivePower  = None
 
    # Governor gain (K<i>)</i>.
    k: PU  = None
 
    # Governor lag time constant (T1).  Typical Value = 0.25.
    t1: Seconds  = None
 
    # Governor lead time constant (T2<i>)</i>.  Typical Value = 0.
    t2: Seconds  = None
 
    # Gate actuator time constant (T3).  Typical Value = 0.1.
    t3: Seconds  = None
 
    # Water starting time (T4). 
    t4: Seconds  = None
 
    # Gate maximum (Pmax). 
    pmax: PU  = None
 
    # Gate minimum (Pmin). 
    pmin: PU  = None
     