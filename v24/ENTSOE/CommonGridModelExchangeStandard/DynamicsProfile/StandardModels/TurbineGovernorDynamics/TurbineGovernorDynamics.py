from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics     

@dataclass
class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """Turbine-governor function block whose behavior is described by reference to a
    standard model <font color="#0f0f0f">or by definition of a user-defined model.
    </font>
    """
    # Asynchronous machine model with which this turbine-governor model is associated.
    AsynchronousMachineDynamics_ref: Optional[AsynchronousMachineDynamics] = None
    AsynchronousMachineDynamics: str = None
 
    # Turbine-governor model associated with this synchronous machine model.
    SynchronousMachineDynamics: List[SynchronousMachineDynamics]  = field(default_factory=list)
     