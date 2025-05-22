from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType4aIEC import WindTurbineType4aIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContPType4aIEC(IdentifiedObject):
    """P control model Type 4A.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.4.
    """
    # Maximum wind turbine power ramp rate (<i>dp</i><sub>max</sub>). It is project
    # dependent parameter.
    dpmax_: PU  = None
 
    # Time constant in power order lag (<i>T</i><sub>pord</sub>). It is type
    # dependent parameter.
    tpord_: Seconds  = None
 
    # Voltage measurement filter time constant (<i>T</i><sub>ufilt</sub>). It is type
    # dependent parameter.
    tufilt_: Seconds  = None
 
    # Wind turbine type 4A model with which this wind control P type 4A model is
    # associated.
    WindTurbineType4aIEC_: Optional[WindTurbineType4aIEC] = None
     