from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenType4IEC import WindGenType4IEC
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindMechIEC import WindMechIEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContPType4bIEC import WindContPType4bIEC     

@dataclass
class WindTurbineType4bIEC(WindGenType4IEC):
    """Wind turbine IEC Type 4A.
    
      Reference: IEC Standard 61400-27-1, section 6.5.5.3.
    """
    # Wind mechanical model associated with this wind turbine Type 4B model.
    WindMechIEC_ref: Optional[WindMechIEC] = None
    WindMechIEC: str = None
 
    # Wind control P type 4B model associated with this wind turbine type 4B model.
    WindContPType4bIEC_ref: Optional[WindContPType4bIEC] = None
    WindContPType4bIEC: str = None
     