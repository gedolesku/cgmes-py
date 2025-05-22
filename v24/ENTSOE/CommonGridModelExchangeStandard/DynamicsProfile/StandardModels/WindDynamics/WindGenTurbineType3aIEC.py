from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType3IEC import WindGenTurbineType3IEC

@dataclass
class WindGenTurbineType3aIEC(WindGenTurbineType3IEC):
    """IEC Type 3A generator set model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.3.2.
    """
    # Current PI controller proportional gain (K<sub>Pc</sub>). It is type dependent
    # parameter.
    kpc: Simple_Float  = None
 
    # Electromagnetic transient reactance (x<sub>S</sub>). It is type dependent
    # parameter.
    xs: PU  = None
 
    # Current PI controller integration time constant (T<sub>Ic</sub>). It is type
    # dependent parameter.
    tic: Seconds  = None
     