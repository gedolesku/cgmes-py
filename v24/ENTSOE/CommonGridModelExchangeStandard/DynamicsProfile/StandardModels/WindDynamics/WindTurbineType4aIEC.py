from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenType4IEC import WindGenType4IEC
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContPType4aIEC import WindContPType4aIEC     

@dataclass
class WindTurbineType4aIEC(WindGenType4IEC):
    """Wind turbine IEC Type 4A.
    
      Reference: IEC Standard 61400-27-1, section 6.5.5.2.
    """
    # Wind control P type 4A model associated with this wind turbine type 4A model.
    WindContPType4aIEC_: Optional[WindContPType4aIEC] = None
     