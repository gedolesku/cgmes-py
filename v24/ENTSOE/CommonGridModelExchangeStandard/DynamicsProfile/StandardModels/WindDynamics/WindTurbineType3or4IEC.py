from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindProtectionIEC import WindProtectionIEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContQIEC import WindContQIEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContCurrLimIEC import WindContCurrLimIEC     

@dataclass
class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """Parent class supporting relationships to IEC wind turbines Type 3 and 4 and
    wind plant including their control models.
    """
    # Wind turbune protection model associated with this wind generator type 3 or 4
    # model.
    WindProtectionIEC_: Optional[WindProtectionIEC] = None
 
    # Wind control Q model associated with this wind turbine type 3 or 4 model.
    WindContQIEC_: Optional[WindContQIEC] = None
 
    # Wind control current limitation model associated with this wind turbine type 3
    # or 4 model.
    WindContCurrLimIEC_: Optional[WindContCurrLimIEC] = None
     