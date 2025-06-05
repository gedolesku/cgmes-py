from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DiscontinuousExcitationControlUserDefined(DiscontinuousExcitationControlDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:DiscontinuousExcitationControlUserDefined.proprietary'})
