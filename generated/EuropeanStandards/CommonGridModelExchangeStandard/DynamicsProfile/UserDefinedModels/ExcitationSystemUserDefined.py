from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcitationSystemUserDefined(ExcitationSystemDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:ExcitationSystemUserDefined.proprietary'})
