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
    parameterNumber: int  = None
 
    # Used for boolean parameter value. If this attribute is populated,
    # integerParameterValue and floatParameterValue will not be.
    booleanParameterValue: bool  = None
 
    # Used for integer parameter value.  If this attribute is populated,
    # booleanParameterValue and floatParameterValue will not be.
    integerParameterValue: int  = None
 
    # Used for floating point parameter value.  If this attribute is populated,
    # booleanParameterValue and integerParameterValue will not be.
    floatParameterValue: Simple_Float  = None
 
    # Proprietary user-defined model with which this parameter is associated.
    LoadUserDefined_ref: Optional[LoadUserDefined] = None
    LoadUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    VoltageCompensatorUserDefined_ref: Optional[VoltageCompensatorUserDefined] = None
    VoltageCompensatorUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType2UserDefined_ref: Optional[PFVArControllerType2UserDefined] = None
    PFVArControllerType2UserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    VoltageAdjusterUserDefined_ref: Optional[VoltageAdjusterUserDefined] = None
    VoltageAdjusterUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType1UserDefined_ref: Optional[PFVArControllerType1UserDefined] = None
    PFVArControllerType1UserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    DiscontinuousExcitationControlUserDefined_ref: Optional[DiscontinuousExcitationControlUserDefined] = None
    DiscontinuousExcitationControlUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    PowerSystemStabilizerUserDefined_ref: Optional[PowerSystemStabilizerUserDefined] = None
    PowerSystemStabilizerUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    UnderexcitationLimiterUserDefined_ref: Optional[UnderexcitationLimiterUserDefined] = None
    UnderexcitationLimiterUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    OverexcitationLimiterUserDefined_ref: Optional[OverexcitationLimiterUserDefined] = None
    OverexcitationLimiterUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    ExcitationSystemUserDefined_ref: Optional[ExcitationSystemUserDefined] = None
    ExcitationSystemUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    MechanicalLoadUserDefined_ref: Optional[MechanicalLoadUserDefined] = None
    MechanicalLoadUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    TurbineLoadControllerUserDefined_ref: Optional[TurbineLoadControllerUserDefined] = None
    TurbineLoadControllerUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    TurbineGovernorUserDefined_ref: Optional[TurbineGovernorUserDefined] = None
    TurbineGovernorUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    AsynchronousMachineUserDefined_ref: Optional[AsynchronousMachineUserDefined] = None
    AsynchronousMachineUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    SynchronousMachineUserDefined_ref: Optional[SynchronousMachineUserDefined] = None
    SynchronousMachineUserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    WindType3or4UserDefined_ref: Optional[WindType3or4UserDefined] = None
    WindType3or4UserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    WindType1or2UserDefined_ref: Optional[WindType1or2UserDefined] = None
    WindType1or2UserDefined: str = None
 
    # Proprietary user-defined model with which this parameter is associated.
    WindPlantUserDefined_ref: Optional[WindPlantUserDefined] = None
    WindPlantUserDefined: str = None
     