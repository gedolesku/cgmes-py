from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantDynamics import WindPlantDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardInterconnections.RemoteInputSignal import RemoteInputSignal     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Wires.EnergySource import EnergySource     

@dataclass
class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """Parent class supporting relationships to wind turbines Type 3 and 4 and wind
    plant including their control models.
    """
    # The wind plant with which the wind turbines type 3 or 4 are associated.
    WindPlantDynamics_: Optional[WindPlantDynamics] = None
 
    # Wind turbine Type 3 or 4 models using this remote input signal.
    RemoteInputSignal_: Optional[RemoteInputSignal] = None
 
    # Energy Source (current source) with which this wind Type 3 or 4 dynamics model
    # is asoociated.
    EnergySource_: Optional[EnergySource] = None
     