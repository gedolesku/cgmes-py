from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class UnderexcitationLimiterUserDefined(UnderexcitationLimiterDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:UnderexcitationLimiterUserDefined.proprietary'})
