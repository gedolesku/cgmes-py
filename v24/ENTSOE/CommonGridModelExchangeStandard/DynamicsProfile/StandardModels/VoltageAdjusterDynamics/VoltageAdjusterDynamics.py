from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics     

@dataclass
class VoltageAdjusterDynamics(DynamicsFunctionBlock):
    """Voltage adjuster function block whose behaviour is described by reference to a
    standard model <font color="#0f0f0f">or by definition of a user-defined model.
    </font>
    """
    # Power Factor or VAr controller Type I model with which this voltage adjuster is
    # associated.
    PFVArControllerType1Dynamics_: Optional[PFVArControllerType1Dynamics] = None
     