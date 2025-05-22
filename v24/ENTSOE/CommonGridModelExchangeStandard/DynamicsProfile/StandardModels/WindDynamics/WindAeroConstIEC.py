from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType1IEC import WindGenTurbineType1IEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindAeroConstIEC(IdentifiedObject):
    """The constant aerodynamic torque model assumes that the aerodynamic torque is
    constant.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.1.1.
    """
    # Wind turbine type 1 model with which this wind aerodynamic model is associated.
    WindGenTurbineType1IEC_: Optional[WindGenTurbineType1IEC] = None
     