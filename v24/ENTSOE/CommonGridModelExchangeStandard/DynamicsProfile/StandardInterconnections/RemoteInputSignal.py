from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    remoteSignalType: RemoteSignalKind  = None
 
    # Power Factor or VAr controller Type I model using this remote input signal.
    PFVArControllerType1Dynamics_ref: Optional[PFVArControllerType1Dynamics] = None
    PFVArControllerType1Dynamics: str = None
 
    # Underexcitation limiter model using this remote input signal.
    UnderexcitationLimiterDynamics_ref: Optional[UnderexcitationLimiterDynamics] = None
    UnderexcitationLimiterDynamics: str = None
 
    # Voltage compensator model using this remote input signal.
    VoltageCompensatorDynamics_ref: Optional[VoltageCompensatorDynamics] = None
    VoltageCompensatorDynamics: str = None
 
    # Power system stabilizer model using this remote input signal.
    PowerSystemStabilizerDynamics_ref: Optional[PowerSystemStabilizerDynamics] = None
    PowerSystemStabilizerDynamics: str = None
 
    # Discontinuous excitation control model using this remote input signal.
    DiscontinuousExcitationControlDynamics_ref: Optional[DiscontinuousExcitationControlDynamics] = None
    DiscontinuousExcitationControlDynamics: str = None
 
    # Remote input signal used by these wind turbine Type 3 or 4 models.
    WindTurbineType3or4Dynamics_ref: Optional[WindTurbineType3or4Dynamics] = None
    WindTurbineType3or4Dynamics: str = None
 
    # The remote signal with which this power plant is associated.
    WindPlantDynamics_ref: Optional[WindPlantDynamics] = None
    WindPlantDynamics: str = None
 
    # Remote terminal with which this input signal is associated.
    Terminal_ref: Optional[Terminal] = None
    Terminal: str = None
     