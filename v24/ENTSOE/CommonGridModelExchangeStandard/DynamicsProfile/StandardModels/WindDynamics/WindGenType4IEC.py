from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC

@dataclass
class WindGenType4IEC(WindTurbineType3or4IEC):
    """IEC Type 4 generator set model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.3.4.
    """
    # Maximum active current ramp rate (di<sub>pmax</sub>). It is project dependent
    # parameter.
    dipmax_: PU  = None
 
    # Minimum reactive current ramp rate (d<i>i</i><sub>qmin</sub>). It is case
    # dependent parameter.
    diqmin_: PU  = None
 
    # Maximum reactive current ramp rate (di<sub>qmax</sub>). It is project dependent
    # parameter.
    diqmax_: PU  = None
 
    # Time constant (T<sub>g</sub>). It is type dependent parameter.
    tg_: Seconds  = None
     