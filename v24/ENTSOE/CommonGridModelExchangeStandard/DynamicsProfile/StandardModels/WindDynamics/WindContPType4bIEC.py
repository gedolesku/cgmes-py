from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType4bIEC import WindTurbineType4bIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContPType4bIEC(IdentifiedObject):
    """P control model Type 4B.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.5.
    """
    # Maximum wind turbine power ramp rate (<i>dp</i><sub>max</sub>). It is project
    # dependent parameter.
    dpmax_: PU  = None
 
    # Time constant in aerodynamic power response (<i>T</i><sub>paero</sub>). It is
    # type dependent parameter.
    tpaero_: Seconds  = None
 
    # Time constant in power order lag (<i>T</i><sub>pord</sub>). It is type
    # dependent parameter.
    tpord_: Seconds  = None
 
    # Voltage measurement filter time constant (<i>T</i><sub>ufilt</sub>). It is type
    # dependent parameter.
    tufilt_: Seconds  = None
 
    # Wind turbine type 4B model with which this wind control P type 4B model is
    # associated.
    WindTurbineType4bIEC_: Optional[WindTurbineType4bIEC] = None
     