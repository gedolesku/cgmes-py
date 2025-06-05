from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Simple_Float import Simple_Float
from .AsynchronousMachineUserDefined import AsynchronousMachineUserDefined
from .DiscontinuousExcitationControlUserDefined import DiscontinuousExcitationControlUserDefined
from .ExcitationSystemUserDefined import ExcitationSystemUserDefined
from .LoadUserDefined import LoadUserDefined
from .MechanicalLoadUserDefined import MechanicalLoadUserDefined
from .OverexcitationLimiterUserDefined import OverexcitationLimiterUserDefined
from .PFVArControllerType1UserDefined import PFVArControllerType1UserDefined
from .PFVArControllerType2UserDefined import PFVArControllerType2UserDefined
from .PowerSystemStabilizerUserDefined import PowerSystemStabilizerUserDefined
from .SynchronousMachineUserDefined import SynchronousMachineUserDefined
from .TurbineGovernorUserDefined import TurbineGovernorUserDefined
from .TurbineLoadControllerUserDefined import TurbineLoadControllerUserDefined
from .UnderexcitationLimiterUserDefined import UnderexcitationLimiterUserDefined
from .VoltageAdjusterUserDefined import VoltageAdjusterUserDefined
from .VoltageCompensatorUserDefined import VoltageCompensatorUserDefined
from .WindPlantUserDefined import WindPlantUserDefined
from .WindType1or2UserDefined import WindType1or2UserDefined
from .WindType3or4UserDefined import WindType3or4UserDefined
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ProprietaryParameterDynamics:
    parameterNumber: Integer = field(metadata={'xpath': 'cim:ProprietaryParameterDynamics.parameterNumber'})
    booleanParameterValue: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:ProprietaryParameterDynamics.booleanParameterValue'})
    floatParameterValue: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:ProprietaryParameterDynamics.floatParameterValue'})
    integerParameterValue: Optional[Integer] = field(default=None, metadata={'xpath': 'cim:ProprietaryParameterDynamics.integerParameterValue'})
    PFVArControllerType1UserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.PFVArControllerType1UserDefined/@rdf:resource", "pattern": r"^#.+$"})
    PFVArControllerType1UserDefined_ref: PFVArControllerType1UserDefined | None = None
    VoltageCompensatorUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.VoltageCompensatorUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    VoltageCompensatorUserDefined_ref: VoltageCompensatorUserDefined | None = None
    MechanicalLoadUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.MechanicalLoadUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    MechanicalLoadUserDefined_ref: MechanicalLoadUserDefined | None = None
    ExcitationSystemUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.ExcitationSystemUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    ExcitationSystemUserDefined_ref: ExcitationSystemUserDefined | None = None
    AsynchronousMachineUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.AsynchronousMachineUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    AsynchronousMachineUserDefined_ref: AsynchronousMachineUserDefined | None = None
    DiscontinuousExcitationControlUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.DiscontinuousExcitationControlUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    DiscontinuousExcitationControlUserDefined_ref: DiscontinuousExcitationControlUserDefined | None = None
    TurbineGovernorUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.TurbineGovernorUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    TurbineGovernorUserDefined_ref: TurbineGovernorUserDefined | None = None
    VoltageAdjusterUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.VoltageAdjusterUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    VoltageAdjusterUserDefined_ref: VoltageAdjusterUserDefined | None = None
    SynchronousMachineUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.SynchronousMachineUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    SynchronousMachineUserDefined_ref: SynchronousMachineUserDefined | None = None
    UnderexcitationLimiterUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.UnderexcitationLimiterUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    UnderexcitationLimiterUserDefined_ref: UnderexcitationLimiterUserDefined | None = None
    TurbineLoadControllerUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.TurbineLoadControllerUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    TurbineLoadControllerUserDefined_ref: TurbineLoadControllerUserDefined | None = None
    OverexcitationLimiterUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.OverexcitationLimiterUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    OverexcitationLimiterUserDefined_ref: OverexcitationLimiterUserDefined | None = None
    PowerSystemStabilizerUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.PowerSystemStabilizerUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    PowerSystemStabilizerUserDefined_ref: PowerSystemStabilizerUserDefined | None = None
    LoadUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.LoadUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    LoadUserDefined_ref: LoadUserDefined | None = None
    PFVArControllerType2UserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.PFVArControllerType2UserDefined/@rdf:resource", "pattern": r"^#.+$"})
    PFVArControllerType2UserDefined_ref: PFVArControllerType2UserDefined | None = None
    WindType3or4UserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.WindType3or4UserDefined/@rdf:resource", "pattern": r"^#.+$"})
    WindType3or4UserDefined_ref: WindType3or4UserDefined | None = None
    WindPlantUserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.WindPlantUserDefined/@rdf:resource", "pattern": r"^#.+$"})
    WindPlantUserDefined_ref: WindPlantUserDefined | None = None
    WindType1or2UserDefined_id: str | None = field(default=None, metadata={"xpath": "cim:ProprietaryParameterDynamics.WindType1or2UserDefined/@rdf:resource", "pattern": r"^#.+$"})
    WindType1or2UserDefined_ref: WindType1or2UserDefined | None = None
