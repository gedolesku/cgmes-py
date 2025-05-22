from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardInterconnections.RemoteInputSignal import RemoteInputSignal     

@dataclass
class VoltageCompensatorDynamics(DynamicsFunctionBlock):
    """Voltage compensator function block whose behaviour is described by reference to
    a standard model <font color="#0f0f0f">or by definition of a user-defined model.
    </font>
    """
    # Excitation system model with which this voltage compensator is associated.
    ExcitationSystemDynamics_ref: Optional[ExcitationSystemDynamics] = None
    ExcitationSystemDynamics: str = None
 
    # Remote input signal used by this voltage compensator model.
    RemoteInputSignal_ref: Optional[RemoteInputSignal] = None
    RemoteInputSignal: str = None
     