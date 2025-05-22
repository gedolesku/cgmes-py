from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardInterconnections.RemoteInputSignal import RemoteInputSignal     

@dataclass
class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """Parent class supporting relationships to wind turbines Type 1 and 2 and their
    control models.
    """
    # Asynchronous machine model with which this wind generator type 1 or 2 model is
    # associated.
    AsynchronousMachineDynamics_: Optional[AsynchronousMachineDynamics] = None
 
    # Remote input signal used by this wind generator Type 1 or Type 2 model.
    RemoteInputSignal_: Optional[RemoteInputSignal] = None
     