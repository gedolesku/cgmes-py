from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.MechanicalLoadDynamics.MechanicalLoadDynamics import MechanicalLoadDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class MechanicalLoadUserDefined(MechanicalLoadDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:MechanicalLoadUserDefined.proprietary'})
