from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindProtectionIEC import WindProtectionIEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindMechIEC import WindMechIEC     

@dataclass
class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """Generator model for wind turbine of IEC Type 1 or Type 2 is a standard
    asynchronous generator model.
    
      Reference: IEC Standard 614000-27-1 Section 6.6.3.1.
    """
    # Wind turbune protection model associated with this wind generator type 1 or 2
    # model.
    WindProtectionIEC_: Optional[WindProtectionIEC] = None
 
    # Wind mechanical model associated with this wind generator type 1 or 2 model.
    WindMechIEC_: Optional[WindMechIEC] = None
     