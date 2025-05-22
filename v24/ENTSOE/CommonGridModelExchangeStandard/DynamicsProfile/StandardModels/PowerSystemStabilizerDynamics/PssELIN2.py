from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssELIN2(PowerSystemStabilizerDynamics):
    """Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or
    Pss2B can also be used).
    """
    # Time constant (Ts1).  Typical Value = 0.
    ts1_: Seconds  = None
 
    # Time constant (Ts2).  Typical Value = 1.
    ts2_: Seconds  = None
 
    # Time constant (Ts3).  Typical Value = 1.
    ts3_: Seconds  = None
 
    # Time constant (Ts4).  Typical Value = 0.1.
    ts4_: Seconds  = None
 
    # Time constant (Ts5).  Typical Value = 0.
    ts5_: Seconds  = None
 
    # Time constant (Ts6).  Typical Value = 1.
    ts6_: Seconds  = None
 
    # Gain (Ks1).  Typical Value = 1.
    ks1_: PU  = None
 
    # Gain (Ks2).  Typical Value = 0.1.
    ks2_: PU  = None
 
    # Coefficient (p_PSS) (>=0 and <=4).  Typical Value = 0.1.
    ppss_: PU  = None
 
    # Coefficient (a_PSS).  Typical Value = 0.1.
    apss_: PU  = None
 
    # PSS limiter (psslim).  Typical Value = 0.1.
    psslim_: PU  = None
     