from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics     

@dataclass
class PFVArControllerType2Dynamics(DynamicsFunctionBlock):
    """Power Factor or VAr controller Type II function block whose behaviour is
    described by reference to a standard model <font color="#0f0f0f">or by
    definition of a user-defined model.</font>
    """
    # Excitation system model with which this Power Factor or VAr controller Type II
    # is associated.
    ExcitationSystemDynamics_: Optional[ExcitationSystemDynamics] = None
     