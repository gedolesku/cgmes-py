from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType3IEC import WindGenTurbineType3IEC

@dataclass
class WindGenTurbineType3bIEC(WindGenTurbineType3IEC):
    """IEC Type 3B generator set model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.3.3.
    """
    # Crowbar duration versus voltage variation look-up table (f<sub>duCW</sub>()).
    # It is case dependent parameter.
    fducw: Simple_Float  = None
 
    # Current generation Time constant (<i>T</i><sub>g</sub>). It is type dependent
    # parameter.
    tg: Seconds  = None
 
    # Time constant for crowbar washout filter (<i>T</i><sub>wo</sub>). It is case
    # dependent parameter.
    two: Seconds  = None
 
    # Crowbar control mode (<i>M</i><sub>WTcwp</sub>).
    # <ul>
    # 	<li>true = 1 in the model</li>
    # 	<li>false = 0 in the model.</li>
    # </ul>
    # The parameter is case dependent parameter.
    mwtcwp: bool  = None
 
    # Electromagnetic transient reactance (x<sub>S</sub>). It is type dependent
    # parameter.
    xs: PU  = None
     