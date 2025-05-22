from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType1or2IEC import WindTurbineType1or2IEC
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindAeroConstIEC import WindAeroConstIEC     

@dataclass
class WindGenTurbineType1IEC(WindTurbineType1or2IEC):
    """Wind turbine IEC Type 1.
    
      Reference: IEC Standard 61400-27-1, section 6.5.2.
    """
    # Wind aerodynamic model associated with this wind turbine type 1 model.
    WindAeroConstIEC_ref: Optional[WindAeroConstIEC] = None
    WindAeroConstIEC: str = None
     