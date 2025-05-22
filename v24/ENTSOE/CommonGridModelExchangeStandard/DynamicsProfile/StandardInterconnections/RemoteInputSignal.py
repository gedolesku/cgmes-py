from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardInterconnections.RemoteSignalKind import RemoteSignalKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import VoltageCompensatorDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantDynamics import WindPlantDynamics     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.Terminal import Terminal     

@dataclass
class RemoteInputSignal(IdentifiedObject):
    """Supports connection to a terminal associated with a remote bus from which an
    input signal of a specific type is coming.
    """
    # Type of input signal.
    remoteSignalType_: RemoteSignalKind  = None
 
    # Power Factor or VAr controller Type I model using this remote input signal.
    PFVArControllerType1Dynamics_: Optional[PFVArControllerType1Dynamics] = None
 
    # Underexcitation limiter model using this remote input signal.
    UnderexcitationLimiterDynamics_: Optional[UnderexcitationLimiterDynamics] = None
 
    # Voltage compensator model using this remote input signal.
    VoltageCompensatorDynamics_: Optional[VoltageCompensatorDynamics] = None
 
    # Power system stabilizer model using this remote input signal.
    PowerSystemStabilizerDynamics_: Optional[PowerSystemStabilizerDynamics] = None
 
    # Discontinuous excitation control model using this remote input signal.
    DiscontinuousExcitationControlDynamics_: Optional[DiscontinuousExcitationControlDynamics] = None
 
    # Remote input signal used by these wind turbine Type 3 or 4 models.
    WindTurbineType3or4Dynamics_: Optional[WindTurbineType3or4Dynamics] = None
 
    # The remote signal with which this power plant is associated.
    WindPlantDynamics_: Optional[WindPlantDynamics] = None
 
    # Remote terminal with which this input signal is associated.
    Terminal_: Optional[Terminal] = None
     