from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardInterconnections.RemoteInputSignal import RemoteInputSignal     

@dataclass
class PowerSystemStabilizerDynamics(DynamicsFunctionBlock):
    """Power system stabilizer function block whose behaviour is described by
    reference to a standard model <font color="#0f0f0f">or by definition of a user-
    defined model.</font>
    """
    # Excitation system model with which this power system stabilizer model is
    # associated.
    ExcitationSystemDynamics_: Optional[ExcitationSystemDynamics] = None
 
    # Remote input signal used by this power system stabilizer model.
    RemoteInputSignal_: List[RemoteInputSignal]  = field(default_factory=list)
     