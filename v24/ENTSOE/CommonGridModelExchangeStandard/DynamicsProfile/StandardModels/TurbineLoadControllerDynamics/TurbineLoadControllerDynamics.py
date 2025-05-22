from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics     

@dataclass
class TurbineLoadControllerDynamics(DynamicsFunctionBlock):
    """Turbine load controller function block whose behavior is described by reference
    to a standard model <font color="#0f0f0f">or by definition of a user-defined
    model.</font>
    """
    # Turbine-governor controlled by this turbine load controller.
    TurbineGovernorDynamics_: Optional[TurbineGovernorDynamics] = None
     