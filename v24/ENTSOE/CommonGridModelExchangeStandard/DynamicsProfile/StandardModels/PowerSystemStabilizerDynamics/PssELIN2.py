from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    ts1: Seconds  = None
 
    # Time constant (Ts2).  Typical Value = 1.
    ts2: Seconds  = None
 
    # Time constant (Ts3).  Typical Value = 1.
    ts3: Seconds  = None
 
    # Time constant (Ts4).  Typical Value = 0.1.
    ts4: Seconds  = None
 
    # Time constant (Ts5).  Typical Value = 0.
    ts5: Seconds  = None
 
    # Time constant (Ts6).  Typical Value = 1.
    ts6: Seconds  = None
 
    # Gain (Ks1).  Typical Value = 1.
    ks1: PU  = None
 
    # Gain (Ks2).  Typical Value = 0.1.
    ks2: PU  = None
 
    # Coefficient (p_PSS) (>=0 and <=4).  Typical Value = 0.1.
    ppss: PU  = None
 
    # Coefficient (a_PSS).  Typical Value = 0.1.
    apss: PU  = None
 
    # PSS limiter (psslim).  Typical Value = 0.1.
    psslim: PU  = None
     