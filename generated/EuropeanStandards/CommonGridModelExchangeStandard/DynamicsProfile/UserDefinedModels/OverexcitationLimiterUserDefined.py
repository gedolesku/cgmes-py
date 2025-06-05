from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class OverexcitationLimiterUserDefined(OverexcitationLimiterDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:OverexcitationLimiterUserDefined.proprietary'})
