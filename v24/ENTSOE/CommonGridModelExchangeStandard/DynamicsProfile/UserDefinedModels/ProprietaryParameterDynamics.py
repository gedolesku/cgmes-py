from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.LoadUserDefined import LoadUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.VoltageCompensatorUserDefined import VoltageCompensatorUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.PFVArControllerType2UserDefined import PFVArControllerType2UserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.VoltageAdjusterUserDefined import VoltageAdjusterUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.PFVArControllerType1UserDefined import PFVArControllerType1UserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.DiscontinuousExcitationControlUserDefined import DiscontinuousExcitationControlUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.PowerSystemStabilizerUserDefined import PowerSystemStabilizerUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.UnderexcitationLimiterUserDefined import UnderexcitationLimiterUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.OverexcitationLimiterUserDefined import OverexcitationLimiterUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.ExcitationSystemUserDefined import ExcitationSystemUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.MechanicalLoadUserDefined import MechanicalLoadUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.TurbineLoadControllerUserDefined import TurbineLoadControllerUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.TurbineGovernorUserDefined import TurbineGovernorUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.AsynchronousMachineUserDefined import AsynchronousMachineUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.SynchronousMachineUserDefined import SynchronousMachineUserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.WindType3or4UserDefined import WindType3or4UserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.WindType1or2UserDefined import WindType1or2UserDefined     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.UserDefinedModels.WindPlantUserDefined import WindPlantUserDefined     

@dataclass
class ProprietaryParameterDynamics:
    """Supports definition of one or more parameters of several different datatypes
    for use by proprietary user-defined models.  NOTE: This class does not inherit
    from IdentifiedObject since it is not intended that a single instance of it be
    referenced by more than one proprietary user-defined model instance.
    """
    # Sequence number of the parameter among the set of parameters associated with
    # the related proprietary user-defined model.
    parameterNumber_: int  = None
 
    # Used for boolean parameter value. If this attribute is populated,
    # integerParameterValue and floatParameterValue will not be.
    booleanParameterValue_: bool  = None
 
    # Used for integer parameter value.  If this attribute is populated,
    # booleanParameterValue and floatParameterValue will not be.
    integerParameterValue_: int  = None
 
    # Used for floating point parameter value.  If this attribute is populated,
    # booleanParameterValue and integerParameterValue will not be.
    floatParameterValue_: Simple_Float  = None
 
    # Proprietary user-defined model with which this parameter is associated.
    LoadUserDefined_: Optional[LoadUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    VoltageCompensatorUserDefined_: Optional[VoltageCompensatorUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType2UserDefined_: Optional[PFVArControllerType2UserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    VoltageAdjusterUserDefined_: Optional[VoltageAdjusterUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType1UserDefined_: Optional[PFVArControllerType1UserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    DiscontinuousExcitationControlUserDefined_: Optional[DiscontinuousExcitationControlUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    PowerSystemStabilizerUserDefined_: Optional[PowerSystemStabilizerUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    UnderexcitationLimiterUserDefined_: Optional[UnderexcitationLimiterUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    OverexcitationLimiterUserDefined_: Optional[OverexcitationLimiterUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    ExcitationSystemUserDefined_: Optional[ExcitationSystemUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    MechanicalLoadUserDefined_: Optional[MechanicalLoadUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    TurbineLoadControllerUserDefined_: Optional[TurbineLoadControllerUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    TurbineGovernorUserDefined_: Optional[TurbineGovernorUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    AsynchronousMachineUserDefined_: Optional[AsynchronousMachineUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    SynchronousMachineUserDefined_: Optional[SynchronousMachineUserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    WindType3or4UserDefined_: Optional[WindType3or4UserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    WindType1or2UserDefined_: Optional[WindType1or2UserDefined] = None
 
    # Proprietary user-defined model with which this parameter is associated.
    WindPlantUserDefined_: Optional[WindPlantUserDefined] = None
     